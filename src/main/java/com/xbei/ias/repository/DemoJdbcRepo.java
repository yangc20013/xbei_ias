package com.xbei.ias.repository;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.xbei.ias.repository.base.BaseJdbcRepo;

@Repository
public class DemoJdbcRepo extends BaseJdbcRepo {
	
	@Autowired
	public DemoJdbcRepo(final DataSource dataSource) {
		super(dataSource);
	}
	
	
//	public String query(final List<String> hrIds){
//		final StringBuffer sql = new StringBuffer();
//        sql.append(" SELECT CONVERT(IFNULL(AVG(c.satisfaction), 0),DECIMAL(10,2)) AS average FROM coach AS c ");
//        sql.append(" WHERE c.`status` = 4 AND c.satisfaction is not null AND c.assign_to_id IN (:hrIds) ");
//
//        final Map<String, List<String>> params = new HashMap<>();
//        params.put("hrIds", "hrIds);
//
//        return getNamedTemplate().queryForObject(sql.toString(), params, String.class);
//	}
}
