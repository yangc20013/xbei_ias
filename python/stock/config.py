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
DROP TABLE IF EXISTS `org_hot_stock`;
CREATE TABLE `org_hot_stock` (
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

insert into org_hot_stock(code,name,goal,date,price)values('300750','宁德时代',91.00,'2019-08-30',71.460);
insert into org_hot_stock(code,name,goal,date,price)values('300073','当升科技',31.59,'2019-08-30',23.480);
insert into org_hot_stock(code,name,goal,date,price)values('600519','贵州茅台',1030.08,'2019-08-30',1125.000);
insert into org_hot_stock(code,name,goal,date,price)values('600887','伊利股份',35.47,'2019-08-30',28.660);
insert into org_hot_stock(code,name,goal,date,price)values('000568','泸州老窖',85.89,'2019-08-30',92.350);
insert into org_hot_stock(code,name,goal,date,price)values('000858','五粮液',121.28,'2019-08-30',138.050);
insert into org_hot_stock(code,name,goal,date,price)values('601012','隆基股份',30.00,'2019-08-30',28.050);
insert into org_hot_stock(code,name,goal,date,price)values('000651','格力电器',63.17,'2019-08-30',55.320);
insert into org_hot_stock(code,name,goal,date,price)values('300760','迈瑞医疗',152.05,'2019-08-30',180.000);
insert into org_hot_stock(code,name,goal,date,price)values('600031','三一重工',16.35,'2019-08-30',13.610);
insert into org_hot_stock(code,name,goal,date,price)values('603288','海天味业',89.39,'2019-08-30',109.390);
insert into org_hot_stock(code,name,goal,date,price)values('000002','万科A',35.90,'2019-08-30',26.200);
insert into org_hot_stock(code,name,goal,date,price)values('002410','广联达',34.15,'2019-08-30',36.190);
insert into org_hot_stock(code,name,goal,date,price)values('002191','劲嘉股份',17.40,'2019-08-30',11.050);
insert into org_hot_stock(code,name,goal,date,price)values('000961','中南建设',11.40,'2019-08-30',7.500);
insert into org_hot_stock(code,name,goal,date,price)values('600104','上汽集团',33.20,'2019-08-30',24.850);
insert into org_hot_stock(code,name,goal,date,price)values('002707','众信旅游',8.28,'2019-08-30',5.500);
insert into org_hot_stock(code,name,goal,date,price)values('601688','华泰证券',25.38,'2019-08-30',19.260);
insert into org_hot_stock(code,name,goal,date,price)values('603808','歌力思',21.68,'2019-08-30',14.500);
insert into org_hot_stock(code,name,goal,date,price)values('002572','索菲亚',26.45,'2019-08-30',18.200);
insert into org_hot_stock(code,name,goal,date,price)values('300251','光线传媒',8.91,'2019-08-30',8.740);
insert into org_hot_stock(code,name,goal,date,price)values('603816','顾家家居',70.08,'2019-08-30',33.850);
insert into org_hot_stock(code,name,goal,date,price)values('002127','南极电商',15.00,'2019-08-30',10.230);
insert into org_hot_stock(code,name,goal,date,price)values('300144','宋城演艺',28.53,'2019-08-30',26.410);
insert into org_hot_stock(code,name,goal,date,price)values('002812','恩捷股份',65.50,'2019-08-30',30.820);
insert into org_hot_stock(code,name,goal,date,price)values('600309','万华化学',52.83,'2019-08-30',45.700);
insert into org_hot_stock(code,name,goal,date,price)values('601628','中国人寿',35.46,'2019-08-30',28.910);
insert into org_hot_stock(code,name,goal,date,price)values('601128','常熟银行',10.29,'2019-08-30',7.520);
insert into org_hot_stock(code,name,goal,date,price)values('000333','美的集团',67.22,'2019-08-30',52.580);
insert into org_hot_stock(code,name,goal,date,price)values('600438','通威股份',0.00,'2019-08-30',15.250);
insert into org_hot_stock(code,name,goal,date,price)values('601100','恒立液压',37.73,'2019-08-30',32.970);
insert into org_hot_stock(code,name,goal,date,price)values('600030','中信证券',0.00,'2019-08-30',22.610);
insert into org_hot_stock(code,name,goal,date,price)values('002531','天顺风能',6.80,'2019-08-30',6.720);
insert into org_hot_stock(code,name,goal,date,price)values('002081','金螳螂',12.60,'2019-08-30',9.700);
insert into org_hot_stock(code,name,goal,date,price)values('002563','森马服饰',15.55,'2019-08-30',11.960);
insert into org_hot_stock(code,name,goal,date,price)values('600872','中炬高新',40.90,'2019-08-30',41.480);
insert into org_hot_stock(code,name,goal,date,price)values('600383','金地集团',15.24,'2019-08-30',11.530);
insert into org_hot_stock(code,name,goal,date,price)values('603899','晨光文具',42.00,'2019-08-30',42.910);
insert into org_hot_stock(code,name,goal,date,price)values('603833','欧派家居',144.00,'2019-08-30',117.030);
insert into org_hot_stock(code,name,goal,date,price)values('002439','启明星辰',32.00,'2019-08-30',30.840);
insert into org_hot_stock(code,name,goal,date,price)values('601933','永辉超市',11.00,'2019-08-30',10.090);
insert into org_hot_stock(code,name,goal,date,price)values('603345','安井食品',45.67,'2019-08-30',49.620);
insert into org_hot_stock(code,name,goal,date,price)values('002371','北方华创',72.00,'2019-08-30',64.150);
insert into org_hot_stock(code,name,goal,date,price)values('002142','宁波银行',27.60,'2019-08-30',22.600);
insert into org_hot_stock(code,name,goal,date,price)values('300137','先河环保',11.60,'2019-08-30',7.640);
insert into org_hot_stock(code,name,goal,date,price)values('002304','洋河股份',145.60,'2019-08-30',110.990);
insert into org_hot_stock(code,name,goal,date,price)values('600048','保利地产',17.30,'2019-08-30',13.790);
insert into org_hot_stock(code,name,goal,date,price)values('300388','国祯环保',12.35,'2019-08-30',9.080);
insert into org_hot_stock(code,name,goal,date,price)values('002624','完美世界',0.00,'2019-08-30',27.840);
insert into org_hot_stock(code,name,goal,date,price)values('600977','中国电影',0.00,'2019-08-30',14.380);


select t.*,(t.goal-t.price)/t.price as 'cb' from org_hot_stock t order by cb desc;

'''