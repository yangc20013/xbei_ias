#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import utils

stock_list = utils.get_stock_list()
for i in stock_list:
	print i
