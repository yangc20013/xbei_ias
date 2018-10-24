#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utils

#主程序
if __name__ == '__main__':
	#utils.db_insert("insert into demo_result(code,name)values('002128','露天煤业')")
	results = utils.db_select("select * from demo_result")
	for row in results:
		print row[0],row[1],row[2]