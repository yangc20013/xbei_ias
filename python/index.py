#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import datetime
import json
import random
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
	user_agent_list=[\
					 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "  
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",  
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "  
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "  
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "  
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",  
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "  
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",  
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "  
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",  
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "  
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",  
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "  
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "  
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
					]
	headers=("user-agent",random.choice(user_agent_list))
	url="http://q.stock.sohu.com/hisHq?code=cn_%s&start=%s&end=%s&stat=1&order=D&period=d&callback=historySearchHandler&rt=json"%(code,bdate,edate)
	response = requests.get(url,headers=headers)
	data = response.text
	parse_data(code,data)

def str2float(s):
	try:
		value = float(s.strip('%'))
		return value/100.0
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