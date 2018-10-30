package com.xbei.ias.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.xbei.ias.models.po.Dict;

@Repository
public interface DictRepo extends CrudRepository<Dict,String>{

}
