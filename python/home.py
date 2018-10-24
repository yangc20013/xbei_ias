#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utils

max=0.5
#主程序
if __name__ == '__main__':
	#stock_list = utils.get_all_stock()#获取所有股票
	stock_list=['000858','300146']
	for code in stock_list:
		data = utils.get_stock_data(code,None,None)
		if data != None:
			stocks = utils.parse_stock(code,data)
			for i in range(0,len(stocks)):
				if utils.str2float(stocks[i][9]) > max:
					print code,stocks[i][0],stocks[i][9]
