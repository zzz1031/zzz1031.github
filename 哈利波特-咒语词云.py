# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:37:52 2021

@author: 14894
"""

import pyecharts
from pyecharts.charts import WordCloud
file_name='./output/哈利波特-咒语词频统计结果.xls'
file=open(file_name,'r')
data=file.readlines()
file.close
#读取咒语词频文件
del data[0]#删除文件标题行

data_list=[]
for line in data:
    line=line.strip()
    line_splited=line.split('\t')
    data_list.append((line_splited[1],line_splited[2]))
print(data_list)
#将读入的每行元素转换成元组储存在列表中

#生成词云
cloud=WordCloud()
cloud.add('',data_list)
out_filename = './output/哈利波特-咒语词云.html'
cloud.render(out_filename)

print('生成结果文件：' + out_filename)


