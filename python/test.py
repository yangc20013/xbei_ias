#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts

def potential_vocanol(name,sta,ed):
    #name='600354'
    df=ts.get_hist_data(name,start=sta,end=ed)
    a=df['turnover'].sum()
    print(name,int(a))
    return a

name='600354'
b1=potential_vocanol(name,'2018-10-14','2018-10-24')

print b1

