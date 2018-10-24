#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utils

stock_list = utils.get_stock_list()
for i in stock_list:
	utils.get_day_stock_info(i,None,None)
