package com.xbei.ias.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.xbei.ias.models.po.DemoChpct;

@Repository
public interface DemoChpctRepo extends CrudRepository<DemoChpct,Long>{

}
