package com.xbei.ias.services.impl;

import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import org.apache.commons.collections.IteratorUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.StringUtils;

import com.alibaba.fastjson.JSONObject;
import com.fasterxml.jackson.databind.JsonNode;
import com.xbei.ias.models.enums.PeriodType;
import com.xbei.ias.models.po.Dict;
import com.xbei.ias.models.po.FilterStock;
import com.xbei.ias.models.po.Stock;
import com.xbei.ias.models.vo.SearchModel;
import com.xbei.ias.repository.DemoJdbcRepo;
import com.xbei.ias.repository.DictRepo;
import com.xbei.ias.repository.FilterStockRepo;
import com.xbei.ias.repository.StockRepo;
import com.xbei.ias.services.StockService;
import com.xbei.ias.utils.DateUtils;
import com.xbei.ias.utils.HttpUtils;
import com.xbei.ias.utils.JSONUtils;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class StockServiceImpl implements StockService {

	@Autowired
	private DictRepo dictRepo;

	@Autowired
	private StockRepo stockRepo;

	@Autowired
	private FilterStockRepo filterStockRepo;

	@Autowired
	private DemoJdbcRepo demoJdbcRepo;

	@Override
	public Dict saveDict(Dict dict) {
		return dictRepo.save(dict);
	}

	@Override
	public List<Dict> findDictByNames(List<String> names) {
		return IteratorUtils.toList(dictRepo.findAllById(names).iterator());
	}

	@Override
	public Dict findDictByName(String name) {
		return dictRepo.findById(name).orElse(null);
	}

	@Transactional
	@Override
	public List<FilterStock> filter(SearchModel model) {
		float dayRate = model.getDayRate();
		float weekRate = model.getWeekRate();
		List<FilterStock> result = new ArrayList<FilterStock>();

		if (model.getStocks() != null && model.getStocks().size() > 0) {
			for (String code : model.getStocks()) {
				FilterStock obj = parseNetworkData(code, dayRate, weekRate);
				if (obj != null) {
					try {
						filterStockRepo.save(obj);
					} catch (Exception e) {
						log.warn("数据已经存在：" + JSONUtils.formatOject2Str(obj));
					}
					result.add(obj);
				}
			}
		} else {
			Iterator<Stock> list = stockRepo.findAll().iterator();
			while (list.hasNext()) {
				Stock stock = list.next();
				FilterStock obj = parseNetworkData(stock.getCode(), dayRate, weekRate);
				if (obj != null) {
					try {
						filterStockRepo.save(obj);
					} catch (Exception e) {
						log.warn("数据已经存在：" + JSONUtils.formatOject2Str(obj));
					}
					result.add(obj);
				}
			}
		}
		return result;
	}
//
//	public static void main(String[] args) {
////		Calendar c = DateUtils.getLastWeekFriday(DateUtils.getCurentDate());
////		System.out.println(DateUtils.formatToDateStr(c.getTime(), null));
//		 StockServiceImpl service = new StockServiceImpl();
//		 service.parseNetworkData("300146", 0.2f, 0.4f);
//	}

	protected JsonNode getNetworkData(String code, PeriodType period) {
		String start = "";
		Date now = DateUtils.getCurentDate();
		if (now.getHours() >= 15) {
			if (period == PeriodType.DAY) {
				start = DateUtils.formatToDateStr(now, null);
			} else if (period == PeriodType.WEEK) {
				start = DateUtils.formatToDateStr(DateUtils.getLastWeekFriday(now).getTime(), null);
			}
		} else {
			if (period == PeriodType.DAY) {
				start = DateUtils.formatToDateStr(DateUtils.getYesterdayOfCurentCalendar().getTime(), null);
			} else if (period == PeriodType.WEEK) {
				start = DateUtils.formatToDateStr(DateUtils.getLastWeekFriday(DateUtils.getCurentDate()).getTime(),
						null);
			}
		}

		String url = String.format(
				"http://q.stock.sohu.com/hisHq?code=cn_%s&start=%s&end=%s&stat=1&order=D&period=%s&callback=historySearchHandler&rt=json",
				code, start, start, period.getName());
		String data = HttpUtils.get(url);
		try {
			JsonNode node = JSONUtils.formatStr2JSONNode(data);
			if (node.get(0).has("status")) {
				return node.get(0).get("hq").get(0);
			}
		} catch (Exception e) {
			log.error("code:" + code + " 获取网络数据出错." + url);
			// throw new RuntimeException("获取网络数据失败, code:"+code);
		}

		return null;
	}

	protected Float string2Num(String s) {
		try {
			NumberFormat numberFormat = NumberFormat.getPercentInstance();
			return numberFormat.parse(s).floatValue();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return 0f;
	}

	protected FilterStock parseNetworkData(String code, float dayRate, float weekRate) {

		FilterStock filterData = new FilterStock();
		filterData.setCode(code);
		boolean isDailyTrue = false, isWeeklyTrue = false;
		JsonNode node = getNetworkData(code, PeriodType.DAY);
		if (node != null) {
			String date = node.get(0).asText();// 日期
			String daily = node.get(9).asText();// 日换手率
			Float f = string2Num(daily);
			if (f == null)
				return null;
			if (f > dayRate) {
				filterData.setDate(date);
				filterData.setDaily(daily);
				isDailyTrue = true;
			}
		}

		node = getNetworkData(code, PeriodType.WEEK);
		if (node != null) {
			String date = node.get(0).asText();// 日期
			String weekly = node.get(9).asText();// 周换手率
			Float f = string2Num(weekly);
			if (f == null)
				return null;
			if (f > weekRate) {
				filterData.setWeekDay(date);
				filterData.setWeekly(weekly);
				isWeeklyTrue = true;
			}
		}

		if (isDailyTrue && isWeeklyTrue)
			return filterData;

		return null;
	}

	@Override
	public List<FilterStock> history() {
		return IteratorUtils.toList(filterStockRepo.findAll().iterator());
	}

	@Override
	public List<FilterStock> today() {
		// TODO Auto-generated method stub
		return filterStockRepo.findToday();
	}

	@Override
	public List<Map<String, Object>> findHotList() {
		return demoJdbcRepo.queryForList("select distinct code,name from org_hot_stock");
	}

	@Override
	public Map<String, Object> findHotStockDetail(List<String> codes) {
		if (StringUtils.isEmpty(codes)) {
			return null;
		}
		
		if(codes.size() == 1) {
			List<Map<String, Object>> list = demoJdbcRepo.queryForList(
					"select name,GROUP_CONCAT(date order by date) date,GROUP_CONCAT(price order by date) price from org_hot_stock where code=? group by name",
					codes.get(0));
			return buildChartData(list);
		}else if(codes.size() > 1) {
			return buildChartData(demoJdbcRepo.queryHotStock(codes));
		} else {
			return null;
		}
//		List<Map<String, Object>> hotList = demoJdbcRepo.queryForList("call pro_get_price()");
//		if (code.equals("10")) {
//			return buildChart(hotList.subList(0, 10));
//		} else {
//			return buildChart(hotList.stream().filter(m -> m.get("code").equals(code)).collect(Collectors.toList()));
//		}
	}

	private Map<String, Object> buildChartData(List<Map<String, Object>> datas) {
		if (datas == null || datas.size() == 0) {
			return null;
		}
		Map<String, Object> result = new HashMap<>();

		List<Map<String, Object>> series = new ArrayList<>();
		for (Map<String, Object> row : datas) {
			Map<String, Object> m = new HashMap<>();
			m.put("name", row.get("name"));
			String[] prices = row.get("price").toString().split(",");
			double[] p = new double[prices.length];

			for (int j = 0; j < prices.length; j++) {
				p[j] = Double.parseDouble(prices[j]);
			}

			m.put("data", p);
			series.add(m);
		}

		result.put("series", series);

		result.put("categories", datas.get(0).get("date").toString().split(","));

		return result;
	}

	private Map<String, Object> buildChart(List<Map<String, Object>> datas) {
		if (datas == null || datas.size() == 0) {
			return null;
		}
		Map<String, Object> result = new HashMap<>();

		JSONObject json = (JSONObject) JSONObject.parse(JSONObject.toJSONString(datas.get(0)));

		String[] strs = { "code", "name", "goal" };
		for (String s : strs) {
			json.remove(s);
		}

		List<Map<String, Object>> series = new ArrayList<>();
		for (Map<String, Object> row : datas) {
			Map<String, Object> m = new HashMap<>();
			m.put("name", row.get("name"));

			for (String s : strs) {
				row.remove(s);
			}

			m.put("data", row.values());
			series.add(m);
		}

		result.put("series", series);

		result.put("categories", json.keySet());

		return result;
	}

}
