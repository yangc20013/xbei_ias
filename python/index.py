#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import datetime
import json
import tushare as ts

max=0.50

def get_stock_list():
	stock_info = ts.get_stock_basics()
	stock_list = []
	for i in stock_info.index: 
		stock_list.append(i)
	return stock_list

def get_day_stock_info(code,bdate,edate):
	if bdate==None:
		now=datetime.datetime.now()
		delta=datetime.timedelta(days=-60)
		n_days=now+delta
		bdate=n_days.strftime('%Y%m%d')
	if edate==None:
		edate=datetime.datetime.now().strftime('%Y%m%d')
	headers=("user-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
	url="http://q.stock.sohu.com/hisHq?code=cn_%s&start=%s&end=%s&stat=1&order=D&period=d&callback=historySearchHandler&rt=json"%(code,bdate,edate)
	response = requests.get(url)
	data = response.text
	parse_data(code,data)

def str2float(s):
	try:
		aa = float(s.strip('%'))
		return aa/100.0
	except Exception,e:
		print(s,e)

def parse_data(code,txt):
	data=json.loads(txt)
	if type(data).__name__ == 'list' and type(data[0]).__name__ == 'dict':
		stocks=data[0]['hq']
		for i in range(0,len(stocks)):
			if str2float(stocks[i][9]) > max:
				print code,stocks[i][0],stocks[i][9]

stock_list = get_stock_list()
for i in stock_list:
	get_day_stock_info(i,None,None)