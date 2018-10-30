package com.xbei.ias.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.xbei.ias.models.po.Stock;

@Repository
public interface StockRepo extends CrudRepository<Stock,String>{

}
