package com.xbei.ias.repository;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import com.xbei.ias.models.po.FilterStock;

public interface FilterStockRepo extends CrudRepository<FilterStock,String>{
	
	@Query("select a from FilterStock a where a.date = (select max(h.date) from FilterStock h)")
	List<FilterStock> findToday();
}
