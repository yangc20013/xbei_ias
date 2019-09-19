package com.xbei.ias.repository;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Repository;

import com.xbei.ias.repository.base.BaseJdbcRepo;

@Repository
public class DemoJdbcRepo extends BaseJdbcRepo {
	
	@Autowired
	public DemoJdbcRepo(final DataSource dataSource) {
		super(dataSource);
	}
	
	protected NamedParameterJdbcTemplate getNamedTemplate() {
		return new NamedParameterJdbcTemplate(this.getDataSource());
	}
	
	
	public List<Map<String ,Object>> queryHotStock(List<String> codes){
		final StringBuffer sql = new StringBuffer();
        sql.append(" SELECT name,GROUP_CONCAT(date order by date) date,GROUP_CONCAT(price order by date) price from org_hot_stock ");
        sql.append(" WHERE code IN (:codes) group by name");

        final Map<String, List<String>> params = new HashMap<>();
        params.put("codes", codes);

        return getNamedTemplate().query(sql.toString(), params, getColumnMapRowMapper());
	}
}
