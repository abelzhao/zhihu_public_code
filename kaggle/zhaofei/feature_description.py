#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
#        Author: ZhaoFei - zhaofei@calfdata.com
#        Create: 2017-09-26 10:12:11
# Last Modified: 2017-09-26 10:12:11
#      Filename: feature_extract.py
#   Description: ---
# Copyright (c) 2016 Chengdu Lanjing Data&Information Co.


from sklearn import preprocessing
import pandas as pd

properties = pd.read_csv("./data/properties_2016.csv", header=0, low_memory=True)
train_2016 = pd.read_csv("./data/train_2016_v2.csv", header=0, low_memory=True)

print properties.head(2)
print train_2016.head(2)
print properties.columns


print "\n airconditioningtypeid: 冷却系统类型"
print properties.airconditioningtypeid.unique()

print "\n basementsqft: 低于地面的建筑面积"
print properties.basementsqft.unique()

print "\n bathroomcnt: 浴室数量"
print properties.bathroomcnt.unique()

print "\n fireplacecnt: 火炉数量"
print properties.fireplacecnt.unique()
des = properties.fireplacecnt.describe()
print des
print properties.fireplacecnt.mean()



#print "\nyearbuilt: 房屋的修建年份"
#print properties.yearbuilt.describe()
## 最新是2015年建立，最老是1801年建立，平均1964年建立
#
#
#print "\nassessmentyear: 房屋的评估年份"
#print properties.assessmentyear.unique()
## 最老是2000年做的评估, 最新是2016年做的评估
#
#
#print "\nlandtaxvaluedollarcnt: 土地价值评估"
#print properties.landtaxvaluedollarcnt.describe()























