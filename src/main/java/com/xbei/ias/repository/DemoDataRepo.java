package com.xbei.ias.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.xbei.ias.models.po.DemoData;

@Repository
public interface DemoDataRepo extends CrudRepository<DemoData,Long>{

}
