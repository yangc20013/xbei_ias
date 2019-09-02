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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (21,'sz300073','当升科技',31.59,'2019-08-30','23.240','2019-08-30 03:03:20');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (21,'sz300750','宁德时代',91,'2019-08-30','70.880','2019-08-30 03:03:21');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (20,'sh600519','贵州茅台',1030.08,'2019-08-30','1141.040','2019-08-30 03:03:22');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (20,'sh600887','伊利股份',35.47,'2019-08-30','28.690','2019-08-30 03:03:23');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (20,'sz000568','泸州老窖',85.89,'2019-08-30','96.860','2019-08-30 03:03:24');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (18,'sz000858','五粮液',121.28,'2019-08-30','141.280','2019-08-30 03:03:25');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sz000651','格力电器',63.17,'2019-08-30','55.780','2019-08-30 03:03:27');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sz300760','迈瑞医疗',152.05,'2019-08-30','185.100','2019-08-30 03:03:28');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sh601012','隆基股份',30,'2019-08-30','27.880','2019-08-30 03:03:29');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sh600031','三一重工',16.35,'2019-08-30','13.500','2019-08-30 03:03:30');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (16,'sh603288','海天味业',89.39,'2019-08-30','114.960','2019-08-30 03:03:31');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (16,'sz000002','万科A',35.9,'2019-08-30','25.830','2019-08-30 03:03:33');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (15,'sz002410','广联达',34.15,'2019-08-30','36.730','2019-08-30 03:03:34');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh603816','顾家家居',70.08,'2019-08-30','33.490','2019-08-30 03:03:35');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz002191','劲嘉股份',17.4,'2019-08-30','11.050','2019-08-30 03:03:36');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz002572','索菲亚',26.45,'2019-08-30','18.330','2019-08-30 03:03:38');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz300251','光线传媒',8.91,'2019-08-30','8.640','2019-08-30 03:03:39');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz000961','中南建设',11.4,'2019-08-30','7.270','2019-08-30 03:03:40');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh600104','上汽集团',33.2,'2019-08-30','25.270','2019-08-30 03:03:42');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz002707','众信旅游',8.28,'2019-08-30','5.390','2019-08-30 03:03:43');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh601688','华泰证券',25.38,'2019-08-30','19.040','2019-08-30 03:03:44');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh603808','歌力思',21.68,'2019-08-30','14.420','2019-08-30 03:03:45');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh600309','万华化学',52.83,'2019-08-30','45.030','2019-08-30 03:03:47');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh601628','中国人寿',35.46,'2019-08-30','28.780','2019-08-30 03:03:48');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh601100','恒立液压',37.73,'2019-08-30','33.080','2019-08-30 03:03:49');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh600438','通威股份',0,'2019-08-30','14.900','2019-08-30 03:03:50');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz002812','恩捷股份',65.5,'2019-08-30','30.390','2019-08-30 03:03:52');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz300144','宋城演艺',28.53,'2019-08-30','26.500','2019-08-30 03:03:53');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh601128','常熟银行',10.29,'2019-08-30','7.350','2019-08-30 03:03:54');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh600030','中信证券',0,'2019-08-30','22.460','2019-08-30 03:03:55');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz000333','美的集团',67.22,'2019-08-30','52.950','2019-08-30 03:03:57');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz002127','南极电商',15,'2019-08-30','10.030','2019-08-30 03:03:58');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh600383','金地集团',15.24,'2019-08-30','11.300','2019-08-30 03:03:59');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002142','宁波银行',27.6,'2019-08-30','22.900','2019-08-30 03:04:00');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002624','完美世界',0,'2019-08-30','27.150','2019-08-30 03:04:02');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh600872','中炬高新',40.9,'2019-08-30','42.390','2019-08-30 03:04:03');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002531','天顺风能',6.8,'2019-08-30','6.530','2019-08-30 03:04:04');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh600048','保利地产',17.3,'2019-08-30','13.510','2019-08-30 03:04:05');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh603899','晨光文具',42,'2019-08-30','42.560','2019-08-30 03:04:06');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh603833','欧派家居',144,'2019-08-30','120.820','2019-08-30 03:04:07');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh603345','安井食品',45.67,'2019-08-30','47.810','2019-08-30 03:04:09');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002563','森马服饰',15.55,'2019-08-30','12.000','2019-08-30 03:04:11');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002439','启明星辰',32,'2019-08-30','30.090','2019-08-30 03:04:12');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh601933','永辉超市',11,'2019-08-30','9.920','2019-08-30 03:04:13');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002081','金螳螂',12.6,'2019-08-30','9.650','2019-08-30 03:04:14');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002371','北方华创',72,'2019-08-30','65.660','2019-08-30 03:04:15');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz300137','先河环保',11.6,'2019-08-30','7.500','2019-08-30 03:04:17');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz300388','国祯环保',12.35,'2019-08-30','9.110','2019-08-30 03:04:18');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002304','洋河股份',145.6,'2019-08-30','112.640','2019-08-30 03:04:19');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (11,'sz300616','尚品宅配',118.19,'2019-08-30','86.150','2019-08-30 03:04:20');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (11,'sz300253','卫宁健康',17.71,'2019-08-30','14.670','2019-08-30 06:45:52');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (21,'sz300073','当升科技',31.59,'2019-09-02','23.920','2019-09-02 06:45:02');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (21,'sz300750','宁德时代',91,'2019-09-02','72.900','2019-09-02 06:45:03');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (20,'sh600519','贵州茅台',1030.08,'2019-09-02','1138.300','2019-09-02 06:45:04');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (20,'sh600887','伊利股份',35.47,'2019-09-02','28.620','2019-09-02 06:45:05');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (20,'sz000568','泸州老窖',85.89,'2019-09-02','97.700','2019-09-02 06:45:06');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (18,'sz000858','五粮液',121.28,'2019-09-02','141.900','2019-09-02 06:45:07');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sz300760','迈瑞医疗',152.05,'2019-09-02','190.990','2019-09-02 06:45:08');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sh600031','三一重工',16.35,'2019-09-02','13.720','2019-09-02 06:45:09');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sh601012','隆基股份',30,'2019-09-02','28.640','2019-09-02 06:45:11');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (17,'sz000651','格力电器',63.17,'2019-09-02','57.760','2019-09-02 06:45:12');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (16,'sz000002','万科A',35.9,'2019-09-02','25.900','2019-09-02 06:45:13');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (16,'sh603288','海天味业',89.39,'2019-09-02','114.000','2019-09-02 06:45:14');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (15,'sz002410','广联达',34.15,'2019-09-02','35.770','2019-09-02 06:45:15');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz002191','劲嘉股份',17.4,'2019-09-02','11.290','2019-09-02 06:45:16');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz000961','中南建设',11.4,'2019-09-02','7.390','2019-09-02 06:45:17');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh600104','上汽集团',33.2,'2019-09-02','24.970','2019-09-02 06:45:18');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz002707','众信旅游',8.28,'2019-09-02','5.420','2019-09-02 06:45:19');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh601688','华泰证券',25.38,'2019-09-02','19.380','2019-09-02 06:45:20');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh603808','歌力思',21.68,'2019-09-02','14.720','2019-09-02 06:45:21');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz300251','光线传媒',8.91,'2019-09-02','9.150','2019-09-02 06:45:22');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sz002572','索菲亚',26.45,'2019-09-02','18.910','2019-09-02 06:45:23');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (14,'sh603816','顾家家居',70.08,'2019-09-02','33.460','2019-09-02 06:45:24');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh600309','万华化学',52.83,'2019-09-02','45.010','2019-09-02 06:45:25');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh601628','中国人寿',35.46,'2019-09-02','28.980','2019-09-02 06:45:26');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh601128','常熟银行',10.29,'2019-09-02','7.400','2019-09-02 06:45:27');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz000333','美的集团',67.22,'2019-09-02','54.460','2019-09-02 06:45:28');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh600438','通威股份',0,'2019-09-02','15.400','2019-09-02 06:45:30');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh601100','恒立液压',37.73,'2019-09-02','33.120','2019-09-02 06:45:31');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sh600030','中信证券',0,'2019-09-02','22.770','2019-09-02 06:45:32');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz002127','南极电商',15,'2019-09-02','10.050','2019-09-02 06:45:33');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz300144','宋城演艺',28.53,'2019-09-02','27.220','2019-09-02 06:45:34');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (13,'sz002812','恩捷股份',65.5,'2019-09-02','30.410','2019-09-02 06:45:35');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002563','森马服饰',15.55,'2019-09-02','11.890','2019-09-02 06:45:36');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh603899','晨光文具',42,'2019-09-02','42.280','2019-09-02 06:45:37');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh600872','中炬高新',40.9,'2019-09-02','42.100','2019-09-02 06:45:38');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh600383','金地集团',15.24,'2019-09-02','11.410','2019-09-02 06:45:39');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh603833','欧派家居',144,'2019-09-02','119.200','2019-09-02 06:45:40');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002439','启明星辰',32,'2019-09-02','31.260','2019-09-02 06:45:42');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh601933','永辉超市',11,'2019-09-02','9.730','2019-09-02 06:45:43');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh603345','安井食品',45.67,'2019-09-02','49.200','2019-09-02 06:45:44');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002142','宁波银行',27.6,'2019-09-02','23.190','2019-09-02 06:45:45');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz300137','先河环保',11.6,'2019-09-02','7.500','2019-09-02 06:45:46');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002371','北方华创',72,'2019-09-02','67.000','2019-09-02 06:45:47');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002304','洋河股份',145.6,'2019-09-02','109.260','2019-09-02 06:45:48');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sh600048','保利地产',17.3,'2019-09-02','13.440','2019-09-02 06:45:49');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz300388','国祯环保',12.35,'2019-09-02','9.170','2019-09-02 06:45:50');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002624','完美世界',0,'2019-09-02','27.470','2019-09-02 06:45:51');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002531','天顺风能',6.8,'2019-09-02','6.900','2019-09-02 06:45:52');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (12,'sz002081','金螳螂',12.6,'2019-09-02','9.770','2019-09-02 06:45:53');
INSERT INTO `org_hot_stock` (`hot`,`code`,`name`,`goal`,`date`,`price`,`created_time`) VALUES (11,'sz002271','东方雨虹',22.79,'2019-09-02','20.490','2019-09-02 06:45:54');

select t.*,(t.goal-t.price)/t.price as 'cb' from org_hot_stock t order by hot desc,cb desc;

select round((t.goal-t.price)/t.price,4) as '差比',t.hot as '关注度',t.code,t.name,t.goal as '目标价',t.price as '当前价',t.date from org_hot_stock t order by 2 desc,1 desc;



CREATE PROCEDURE `pro_get_price`()
BEGIN
	SET @sql = NULL;
	SELECT 
    GROUP_CONCAT(DISTINCT CONCAT('MAX(IF(s.date = \'',
                c.date,
                '\', s.price, 0)) AS \'',
                c.date,
                '\''))
INTO @sql FROM
    org_hot_stock c;

	SET @sql = CONCAT('Select st.code, st.name, st.goal,', @sql, 
							' From org_hot_stock  st Left Join org_hot_stock s On st.code = s.code
							Group by 1,2');
	PREPARE stmt FROM @sql;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;
END

call pro_get_price();
'''