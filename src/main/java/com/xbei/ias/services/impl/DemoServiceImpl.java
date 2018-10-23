package com.xbei.ias.services.impl;

import java.util.List;
import java.util.Map;

import org.apache.commons.collections.IteratorUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import com.xbei.ias.models.po.DemoChpct;
import com.xbei.ias.models.po.DemoData;
import com.xbei.ias.models.po.DemoResult;
import com.xbei.ias.repository.DemoChpctRepo;
import com.xbei.ias.repository.DemoDataRepo;
import com.xbei.ias.repository.DemoJdbcRepo;
import com.xbei.ias.repository.DemoResultRepo;
import com.xbei.ias.services.DemoService;

@Service
public class DemoServiceImpl implements DemoService{
	
	@Autowired
	private DemoResultRepo demoResultRepo;
	
	@Autowired
	private DemoDataRepo demoDataRepo;
	
	@Autowired
	private DemoChpctRepo demmChpctRepo;
	
	@Autowired
	private DemoJdbcRepo demoJdbcRepo;

	@Override
	public Page<DemoResult> getResult(Pageable pageable) {
		return demoResultRepo.findAll(pageable);
				
	}

	@Override
	public List<DemoData> getData() {
		return IteratorUtils.toList(demoDataRepo.findAll().iterator());
	}

	@Override
	public List<DemoChpct> getChpct() {
		return IteratorUtils.toList(demmChpctRepo.findAll().iterator());
	}

	@Override
	public List<Map<String, Object>> getEtop() {
		return demoJdbcRepo.queryForList("select * from demo_etop");
	}

	@Override
	public List<Map<String, Object>> getOrisignal() {
		return demoJdbcRepo.queryForList("select * from demo_orisignal");
	}

}
