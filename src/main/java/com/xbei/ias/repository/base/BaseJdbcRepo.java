package com.xbei.ias.repository.base;

import javax.sql.DataSource;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;

public class BaseJdbcRepo  extends JdbcTemplate{
	public BaseJdbcRepo(DataSource dataSource) {
		super(dataSource);
	}
	
	protected NamedParameterJdbcTemplate getNamedTemplate() {
		return new NamedParameterJdbcTemplate(this.getDataSource());
	}
}
