package com.xbei.ias.services;

import java.util.List;

import com.xbei.ias.models.po.Dict;
import com.xbei.ias.models.po.FilterStock;
import com.xbei.ias.models.vo.SearchModel;

public interface StockService {
	Dict saveDict(Dict dict);
	List<Dict> findDictByNames(List<String> names);
	
	Dict findDictByName(String name);
	List<FilterStock> filter(SearchModel model);
	List<FilterStock> history();
	List<FilterStock> today();
}
