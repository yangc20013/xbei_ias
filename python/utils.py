#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import requests
import datetime
import json
import pymysql
import config

#获取所有股票
def get_all_stock():
	stock_info = ts.get_stock_basics()
	stock_list = []
	for i in stock_info.index: 
		stock_list.append(i)
	return stock_list
'''
调用souhu接口，获取某只股票的数据
code:股票代码
bdate:开始日期 20181010
ddate:结束日期 20181025
'''
def get_stock_data(code,bdate,edate):
	if bdate is None:
		now=datetime.datetime.now()
		delta=datetime.timedelta(days=-60)
		n_days=now+delta
		bdate=n_days.strftime('%Y%m%d')
	if edate is None:
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
	url="http://q.stock.sohu.com/hisHq?code=cn_%s&start=%s&end=%s&stat=1&order=D&period=d&callback=historySearchHandler&rt=json"%(code,bdate,edate)
	try:
		headers={"user-agent":random.choice(user_agent_list)}
		
		response = requests.get(url,headers=headers)
		content = response.text
		return content
	except Exception,e:
		print("error: "+url)
	return None
#带百分号的字符串转float
def str2float(s):
	try:
		value = float(s.strip('%'))
		return value/100.0
	except Exception,e:
		print(s,e)
'''
解析数据
code:股票代码
txt:[{"status":0,
  "hq":[["2018-10-23","20.19","19.26","-1.13","-5.54%","18.96","20.19","364248","71199.58","4.14%"],
				   ["2018-10-22","18.78","20.39","1.85","9.98%","18.78","20.39","396375","79616.41","4.51%"]],
  "code":"cn_300146",
  "stat":["累计:","2018-10-22至2018-10-23","1.08","5.94%",17.68,20.39,1075893,208318.74,"12.24%"]}]
'''
def parse_stock(code,txt):
	data=json.loads(txt)
	if type(data).__name__ == 'list' and type(data[0]).__name__ == 'dict':
		return data[0]['hq']
	return None

#execute insert
def db_insert(sql):
	try:
		db=pymysql.connect(host=config.MYSQL_HOST,user=config.MYSQL_USER,password=config.MYSQL_PASSWORD,db=config.MYSQL_DB,charset='utf8',port=config.MYSQL_PORT)
		cur = db.cursor()
		cur.execute(sql)
		db.commit()
		db.close()
	except Exception as e:
		print('error, '+str(e))
#execute select
def db_select(sql):
	try:
		db=pymysql.connect(host=config.MYSQL_HOST,user=config.MYSQL_USER,password=config.MYSQL_PASSWORD,db=config.MYSQL_DB,charset='utf8',port=config.MYSQL_PORT)
		cur = db.cursor()
		cur.execute(sql)
		results = cur.fetchall()	#获取查询的所有记录
		db.close()
		return results
	except Exception as e:
		print('error, '+str(e))
