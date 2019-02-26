#coding=utf-8

import requests
from lxml import etree

#打开网页，获取网页内容
def url_open(url):
    headers=("user-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text
    return data

#将数据存入mysql中
def data_Import(sql):
    db=pymysql.connect(host='localhost',user='root',password='root',db='python',charset='utf8',port=3306)
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()

if __name__=='__main__':
    url="http://app.finance.ifeng.com/data/stock/tab_zjlx.php?code=sz000050"
    data=url_open(url)
    html = etree.HTML(data,etree.HTMLParser())

    for index in range(2,15):
        s_date = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[1]/text()')[0]
        s_all = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[2]/span/text()')[0].replace('万元','')
        s_sh = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[3]/span/text()')[0]
        s_zh = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[4]/span/text()')[0]
        s_dh = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[5]/span/text()')[0]
        s_cd = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[6]/span/text()')[0]
        s_cje = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[7]/text()')[0]
        s_zdf = html.xpath('//table[@class="lable_tab01"]/tbody/tr['+str(index)+']/td[8]/span/text()')[0]
        
        print(s_date,s_all,s_sh,s_zh,s_dh,s_cd,s_cje,s_zdf)
        
print("任务完成")

