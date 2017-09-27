#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
#        Author: ZhaoFei - zhaofei@calfdata.com
#        Create: 2017-09-27 10:30:10
# Last Modified: 2017-09-27 10:30:10
#      Filename: dataset_etl.py
#   Description: ---
# Copyright (c) 2016 Chengdu Lanjing Data&Information Co.


"""
1. 将properties和train合并, 整理出训练样本

"""

## step 2. 预处理train的特征因子及预测目标
#train = pd.read_csv("./data/train_v2.csv", header=0, low_memory=True)
#train.index = train.parcelid
#
#train_datasets = pd.merge(properties, train, on='parcelid', how='inner')
#del properties, train

#testdata = pd.DataFrame({'pet':['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'cat', 'fish'],
#                      'age': [4, 6, 3, 3, 2, 3, 5, 4],
#                      'salary':  [90, 24, 44, 27, 32, 59, 36, 27]})
#print testdata
#
#print ""
#
#mapper = DataFrameMapper([('pet', LabelBinarizer()),
#                          (['salary'], MinMaxScaler()),
#                          (['age'], OneHotEncoder())])
#fited_data =  mapper.fit_transform(testdata)
#print pd.DataFrame(fited_data)


import numpy as np
import pandas as pd
from sklearn.preprocessing import *
from sklearn_pandas import DataFrameMapper

DATA_DIR = "./data/"

# step 1. 预处理properties的特征因子
properties = pd.read_csv(DATA_DIR+"properties_2016.csv", header=0, low_memory=False)
properties.index = properties.parcelid

print properties.columns

# 1) *id字段: 离散类型, one-hot编码
def onehot_id(id):
    if np.isnan(id):
        return str(1000000)
    else:
        return str(id)


ID_Feature_Columns = ['airconditioningtypeid',         # 空调类型
                      'architecturalstyletypeid',      # 建筑风格类型
                      'buildingqualitytypeid',         # 建筑质量类型
                      'buildingclasstypeid',           # 建筑框架类型
                      'decktypeid',                    # 甲板类型
                      'heatingorsystemtypeid',         # 供暖系统类型
                      'propertylandusetypeid',         # 土地使用类型
                      'storytypeid',                   # 楼层类型
                      'typeconstructiontypeid'         # 建筑材料类型
                      ]
Mapper_Items = []

for id_column in ID_Feature_Columns:
    properties[id_column] = properties[id_column].apply(lambda x: onehot_id(x))

Mapper_Items.append((ID_Feature_Columns, OneHotEncoder()))


# 2) *cnt字段: 连续类型, MinMax编码, nan取中值
def minmax_cnt(cnt, mean_cnt):
    if np.isnan(cnt):
        return mean_cnt
    else:
        return cnt

CNT_Feature_Columns = ['bathroomcnt',    # 家庭浴室数量
                       'bedroomcnt',     # 卧室数量
                       'fireplacecnt',   # 火炉数量
                       'fullbathcnt',    # 全套浴室数量
                       'garagecarcnt',   # 停车场数量
                       'poolcnt',        # 游泳池数量
                       'roomcnt',        # 总房间数量
                       'unitcnt',        # 单元数量
                       'taxvaluedollarcnt', # 税收价值
                       'structuretaxvaluedollarcnt', # 结构税收价值
                       'landtaxvaluedollarcnt' # 土地面积价值
                      ]

for cnt_column in CNT_Feature_Columns:
    cnt_mean = properties[cnt_column].mean()
    print cnt_mean
    properties[cnt_column] = properties[cnt_column].apply(lambda x: minmax_cnt(x, cnt_mean))

Mapper_Items.append((CNT_Feature_Columns, MinMaxScaler()))

# last) 基于DataFrameMapper做特征工程

mapper = DataFrameMapper(Mapper_Items)
datasets = pd.DataFrame(mapper.fit_transform(properties))
print datasets









