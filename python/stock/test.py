#!/usr/bin/python
# -*- coding: UTF-8 -*-
import util,re

def get_stock_price(code):
	url = "http://hq.sinajs.cn/list=%s"%(code)
	pageSource = util.get_page_source(url)
	if pageSource != None:
		s = re.match(".*\"(.*)\".*",str(pageSource))
		hq_str = s.group(1)
		stock_info = hq_str.split(",")
		return stock_info[3]
	return None

if __name__ == '__main__':
    sql = "select * from org_hot_stock where date='2019-08-30'"
    results = util.db_select(sql)
    for row in results:
        print(row[2],row[3],row[4], row[6],get_stock_price(row[2]))