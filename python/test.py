#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utils
import tushare as ts

if __name__ == '__main__':
	stock_info = ts.get_stock_basics()
	sql="insert into stock(code,name)values"
	l = len(stock_info)
	c = 0
	for i in stock_info.index:
		c = c+1
		if c == l:
			sql = sql + '(\'' + i + '\',\'' + stock_info['name'][i]+'\')'
		else:
			sql = sql + '(\'' + i + '\',\'' + stock_info['name'][i]+'\'),'
	print sql
	utils.db_insert(sql)

