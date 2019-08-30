#!/usr/bin/python
# -*- coding: UTF-8 -*-
import util,re,time,logging
from bs4 import BeautifulSoup


# sian 接口返回数据
# 0：”大秦铁路”，股票名字；
# 1：”27.55″，今日开盘价；
# 2：”27.25″，昨日收盘价；
# 3：”26.91″，当前价格；
# 4：”27.55″，今日最高价；
# 5：”26.20″，今日最低价；
# 6：”26.91″，竞买价，即“买一”报价；
# 7：”26.92″，竞卖价，即“卖一”报价；
# 8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值
# 除以一百；
# 9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，
# 所以通常把该值除以一万；
# 10：”4695″，“买一”申请4695股，即47手；
# 11：”26.91″，“买一”报价；
# 12：”57590″，“买二”
# 13：”26.90″，“买二”
# 14：”14700″，“买三”
# 15：”26.89″，“买三”
# 16：”14300″，“买四”
# 17：”26.88″，“买四”
# 18：”15100″，“买五”
# 19：”26.87″，“买五”
# 20：”3100″，“卖一”申报3100股，即31手；
# 21：”26.92″，“卖一”报价
# (22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
# 30：”2008-01-11″，日期；
# 31：”15:05:32″，时间；

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_stock_price(code):
	url = "http://hq.sinajs.cn/list=%s"%(code)
	pageSource = util.get_page_source(url)
	if pageSource != None:
		s = re.match(".*\"(.*)\".*",str(pageSource))
		hq_str = s.group(1)
		stock_info = hq_str.split(",")
		return stock_info[3]
	return None

#主程序
if __name__ == '__main__':
	url="http://app.finance.ifeng.com/report/hot.php"
	pageSource = util.get_page_source(url)
	if pageSource != None:
		soup=BeautifulSoup(pageSource,'html.parser')
		rows = soup.select(".newsHybg .list2 tr")
		for row in rows:
			try:
				td = row.select("td")
				name = td[1].get_text()
				target = td[8].get_text()
				searchCode = re.match(".*code=(\\d{6}).*",str(td))
				code=searchCode.group(1)
				searchStock = re.match(".*id=\"([a-z]{2}\\d{6}).*",str(td))
				price = get_stock_price(searchStock.group(1))
				if(int(float(price)) == 0):
					logger.warning(code + " " + name+ " price = 0")
					continue
				
				sql = "insert into org_hot_stock(code,name,goal,date,price)values('%s','%s',%s,'%s',%s)"%(code,name,target,time.strftime("%Y-%m-%d",time.localtime()),price)
				util.db_insert(sql)
				# print(sql)
				time.sleep(1)
			except Exception as e:
				logger.error(row)
	# url="http://finance.ifeng.com/app/hq/stock/sh601012/index.shtml"
	# pageSource = util.get_page_source(url)
	# if pageSource != None:
	# 	soup=BeautifulSoup(pageSource,'html.parser')
	# 	#print(soup.select('#hyzd06-2'))
	# 	rows = soup.select("#hyzd06-2 .tabTd")
	# 	for row in rows:
	# 		td = row.select("td")
	# 		name = td[0].get_text()
	# 		target = td[2].get_text()
	# 		searchStock = re.match(".*code=([a-z]{2}\\d{6}).*",str(td))
	# 		price = get_stock_price(searchStock.group(1))
	# 		searchCode = re.match(".*code=(\\d{6}).*",str(td))
	# 		code=searchCode.group(1)
	# 		# print(code,name,target,price)
	# 		sql = "insert into org_concern_stock(code,name,goal,date,price)values('%s','%s',%s,'%s',%s)"%(code,name,target,time.strftime("%Y-%m-%d",time.localtime()),price)
	# 		util.db_insert(sql)
	# 		#print(sql)
logger.info("execute final.")


