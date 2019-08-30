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
  `hot` int NOT NULL,
  `code` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `goal` float NOT NULL,
  `date` date NOT NULL,
  `price` varchar(45) DEFAULT NULL,
  `created_time` timestamp DEFAULT NOW(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `index2` (`code`,`date`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

insert into org_hot_stock(hot,code,name,goal,date,price)values(21,'300073','当升科技',31.59,'2019-08-30',23.240);
insert into org_hot_stock(hot,code,name,goal,date,price)values(21,'300750','宁德时代',91.00,'2019-08-30',70.880);
insert into org_hot_stock(hot,code,name,goal,date,price)values(20,'600519','贵州茅台',1030.08,'2019-08-30',1141.040);
insert into org_hot_stock(hot,code,name,goal,date,price)values(20,'600887','伊利股份',35.47,'2019-08-30',28.690);
insert into org_hot_stock(hot,code,name,goal,date,price)values(20,'000568','泸州老窖',85.89,'2019-08-30',96.860);
insert into org_hot_stock(hot,code,name,goal,date,price)values(18,'000858','五粮液',121.28,'2019-08-30',141.280);
insert into org_hot_stock(hot,code,name,goal,date,price)values(17,'000651','格力电器',63.17,'2019-08-30',55.780);
insert into org_hot_stock(hot,code,name,goal,date,price)values(17,'300760','迈瑞医疗',152.05,'2019-08-30',185.100);
insert into org_hot_stock(hot,code,name,goal,date,price)values(17,'601012','隆基股份',30.00,'2019-08-30',27.880);
insert into org_hot_stock(hot,code,name,goal,date,price)values(17,'600031','三一重工',16.35,'2019-08-30',13.500);
insert into org_hot_stock(hot,code,name,goal,date,price)values(16,'603288','海天味业',89.39,'2019-08-30',114.960);
insert into org_hot_stock(hot,code,name,goal,date,price)values(16,'000002','万科A',35.90,'2019-08-30',25.830);
insert into org_hot_stock(hot,code,name,goal,date,price)values(15,'002410','广联达',34.15,'2019-08-30',36.730);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'603816','顾家家居',70.08,'2019-08-30',33.490);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'002191','劲嘉股份',17.40,'2019-08-30',11.050);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'002572','索菲亚',26.45,'2019-08-30',18.330);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'300251','光线传媒',8.91,'2019-08-30',8.640);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'000961','中南建设',11.40,'2019-08-30',7.270);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'600104','上汽集团',33.20,'2019-08-30',25.270);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'002707','众信旅游',8.28,'2019-08-30',5.390);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'601688','华泰证券',25.38,'2019-08-30',19.040);
insert into org_hot_stock(hot,code,name,goal,date,price)values(14,'603808','歌力思',21.68,'2019-08-30',14.420);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'600309','万华化学',52.83,'2019-08-30',45.030);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'601628','中国人寿',35.46,'2019-08-30',28.780);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'601100','恒立液压',37.73,'2019-08-30',33.080);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'600438','通威股份',0.00,'2019-08-30',14.900);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'002812','恩捷股份',65.50,'2019-08-30',30.390);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'300144','宋城演艺',28.53,'2019-08-30',26.500);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'601128','常熟银行',10.29,'2019-08-30',7.350);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'600030','中信证券',0.00,'2019-08-30',22.460);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'000333','美的集团',67.22,'2019-08-30',52.950);
insert into org_hot_stock(hot,code,name,goal,date,price)values(13,'002127','南极电商',15.00,'2019-08-30',10.030);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'600383','金地集团',15.24,'2019-08-30',11.300);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002142','宁波银行',27.60,'2019-08-30',22.900);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002624','完美世界',0.00,'2019-08-30',27.150);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'600872','中炬高新',40.90,'2019-08-30',42.390);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002531','天顺风能',6.80,'2019-08-30',6.530);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'600048','保利地产',17.30,'2019-08-30',13.510);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'603899','晨光文具',42.00,'2019-08-30',42.560);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'603833','欧派家居',144.00,'2019-08-30',120.820);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'603345','安井食品',45.67,'2019-08-30',47.810);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002563','森马服饰',15.55,'2019-08-30',12.000);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002439','启明星辰',32.00,'2019-08-30',30.090);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'601933','永辉超市',11.00,'2019-08-30',9.920);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002081','金螳螂',12.60,'2019-08-30',9.650);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002371','北方华创',72.00,'2019-08-30',65.660);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'300137','先河环保',11.60,'2019-08-30',7.500);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'300388','国祯环保',12.35,'2019-08-30',9.110);
insert into org_hot_stock(hot,code,name,goal,date,price)values(12,'002304','洋河股份',145.60,'2019-08-30',112.640);
insert into org_hot_stock(hot,code,name,goal,date,price)values(11,'300616','尚品宅配',118.19,'2019-08-30',86.150);

select t.*,(t.goal-t.price)/t.price as 'cb' from org_hot_stock t order by hot desc,cb desc;

'''