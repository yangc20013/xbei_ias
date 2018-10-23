package com.xbei.ias.repository;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

import com.xbei.ias.models.po.DemoResult;

@Repository
public interface DemoResultRepo extends PagingAndSortingRepository<DemoResult,Long>{

}
