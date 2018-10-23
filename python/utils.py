#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts

def get_stock_list():
	stock_info = ts.get_stock_basics()
	stock_list = []
	for i in stock_info.index: 
		stock_list.append(i)
	return stock_list

def get_hist_turnover(code):
	info = ts.get_hist_data(code).head(10)
	print info
	for i in range(0,len(info)):
		print info.index[i],info['open'][i]
	#for date in info.index:
	#	print info[date]