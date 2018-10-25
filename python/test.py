#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import os

symbols = ts.get_stock_basics().head(1)
st = ts.get_st_classified()
lv_price_1 = 50

def isSt(stockID):
	for sti in st.code:
		if sti == stockID:
			return True
		return False
	
for inx in range(len(symbols)):
	symbol = symbols.index[inx]
	print symbol
	df = ts.get_k_data(symbol, ktype='60', end='2018-09-21')
	print df
	for item in df.index:
		print df.ix[1]['date']
	
	xn = len(df.index)-1
	#过滤停牌
	if type(df) != type(None) and xn >= 0 and df.ix[xn]['date'] != '2018-10-21':
		continue
	#过滤高价股
	if type(df) != type(None) and xn >= 0 and df.ix[xn]['close'] > lv_price_1:
		continue
	#过滤PE
	pe = symbols.ix[inx]['pe']
	if pe < 20:
		continue
	#过滤ST
	if isSt(symbol):
		continue
	#print inx
