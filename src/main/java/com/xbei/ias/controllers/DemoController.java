package com.xbei.ias.controllers;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.xbei.ias.models.po.DemoChpct;
import com.xbei.ias.models.po.DemoData;
import com.xbei.ias.models.po.DemoResult;
import com.xbei.ias.models.po.Dict;
import com.xbei.ias.models.po.FilterStock;
import com.xbei.ias.models.vo.SearchModel;
import com.xbei.ias.services.DemoService;
import com.xbei.ias.services.StockService;


@RestController
@RequestMapping(value = "/demo")
public class DemoController {
	
	@Autowired
	private DemoService demoService;
	
	@SuppressWarnings("deprecation")
	@RequestMapping(value = "/result", method = RequestMethod.GET)
    public ResponseEntity<Page<DemoResult>> result(SearchModel model) {
//		Pageable pageable = new PageRequest(model.getPageNum() - 1,model.getPageSize(), new Sort(model.getOrder(),model.getSortColumn()));
		
		Pageable pageable = new PageRequest(model.getPageNum() - 1,model.getPageSize());
		return new ResponseEntity<>(demoService.getResult(pageable),HttpStatus.OK);
	}
	
	@RequestMapping(value = "/data", method = RequestMethod.GET)
	public ResponseEntity<List<DemoData>> data() {
		
		return new ResponseEntity<>(demoService.getData(),HttpStatus.OK);
	}
	
	@RequestMapping(value = "/chpct", method = RequestMethod.GET)
	public ResponseEntity<List<DemoChpct>> chpct() {
		
		return new ResponseEntity<>(demoService.getChpct(),HttpStatus.OK);
	}
	
	@RequestMapping(value = "/etop", method = RequestMethod.GET)
	public ResponseEntity<List<Map<String,Object>>> etop() {
		
		return new ResponseEntity<>(demoService.getEtop(),HttpStatus.OK);
	}
	@RequestMapping(value = "/orisignal", method = RequestMethod.GET)
	public ResponseEntity<List<Map<String,Object>>> orisignal() {
		
		return new ResponseEntity<>(demoService.getOrisignal(),HttpStatus.OK);
	}
	//////////////////////////////////////////////////////////////////
	///////////////////// Stock controller ///////////////////////////
	//////////////////////////////////////////////////////////////////
	@Autowired
	private StockService stockService;
	
	@RequestMapping(value = "/config", method = RequestMethod.GET)
	public ResponseEntity<List<Dict>> config(@RequestParam(value="names[]") List<String> names) {
		return new ResponseEntity<>(stockService.findDictByNames(names),HttpStatus.OK);
	}
	@RequestMapping(value = "/saveConfig", method = RequestMethod.POST)
	public ResponseEntity<String> saveConfig(@RequestBody List<Dict> dicts) {
		for(Dict d : dicts) {
			stockService.saveDict(d);
		}
		return new ResponseEntity<>("保存成功",HttpStatus.NO_CONTENT);
	}
	
	@RequestMapping(value = "/parse", method = RequestMethod.POST)
	public ResponseEntity<List<FilterStock>> parse(@RequestBody SearchModel rate) {
		List<FilterStock> list = stockService.filter(rate);
		return new ResponseEntity<>(list,HttpStatus.OK);
	}
	@RequestMapping(value = "/history", method = RequestMethod.GET)
	public ResponseEntity<List<FilterStock>> history() {
		List<FilterStock> list = stockService.history();
		return new ResponseEntity<>(list,HttpStatus.OK);
	}
	@RequestMapping(value = "/today", method = RequestMethod.GET)
	public ResponseEntity<List<FilterStock>> today() {
		List<FilterStock> list = stockService.today();
		return new ResponseEntity<>(list,HttpStatus.OK);
	}
	
	
}
