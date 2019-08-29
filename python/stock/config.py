#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

# mysql数据库连接信息
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'my_python'

'''
CREATE DATABASE  IF NOT EXISTS `my_python` ;
USE `my_python`;
DROP TABLE IF EXISTS `org_concern_stock`;
CREATE TABLE `org_concern_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `goal` float NOT NULL,
  `date` date NOT NULL,
  `price` varchar(45) DEFAULT NULL,
  `created_time` timestamp DEFAULT NOW(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `index2` (`code`,`date`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

insert into org_concern_stock(code,name,goal,date,price)values('300073','当升科技',31.59,'2019-08-29',23.310);
insert into org_concern_stock(code,name,goal,date,price)values('300750','宁德时代',91.00,'2019-08-29',71.080);
insert into org_concern_stock(code,name,goal,date,price)values('600887','伊利股份',35.47,'2019-08-29',29.100);
insert into org_concern_stock(code,name,goal,date,price)values('000568','泸州老窖',85.89,'2019-08-29',92.280);
insert into org_concern_stock(code,name,goal,date,price)values('600519','贵州茅台',1030.08,'2019-08-29',1113.100);
insert into org_concern_stock(code,name,goal,date,price)values('000858','五粮液',121.28,'2019-08-29',137.000);
insert into org_concern_stock(code,name,goal,date,price)values('000651','格力电器',63.17,'2019-08-29',54.780);
insert into org_concern_stock(code,name,goal,date,price)values('600031','三一重工',16.35,'2019-08-29',13.460);
insert into org_concern_stock(code,name,goal,date,price)values('300760','迈瑞医疗',152.05,'2019-08-29',179.080);
insert into org_concern_stock(code,name,goal,date,price)values('601012','隆基股份',30.00,'2019-08-29',27.650);

select t.*,(t.goal-t.price)/t.price as 'cb' from org_concern_stock t order by cb desc;

'''