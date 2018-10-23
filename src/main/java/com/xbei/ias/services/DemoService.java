package com.xbei.ias.services;

import java.util.List;
import java.util.Map;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import com.xbei.ias.models.po.DemoChpct;
import com.xbei.ias.models.po.DemoData;
import com.xbei.ias.models.po.DemoResult;

public interface DemoService {
	Page<DemoResult> getResult(Pageable pageable);

	List<DemoData> getData();

	List<DemoChpct> getChpct();

	List<Map<String,Object>> getEtop();

	List<Map<String,Object>> getOrisignal();
}
