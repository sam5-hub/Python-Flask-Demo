# __author__ == ''
# -*- coding: utf-8 -*-

#app目录是来存放应用的
#static是存放js,css等文件
#template存放html,模板生成文件
#__init__ models是数据模型 views是视图相关的

#做为一个python的包,主要开发的地方
#worker_class="gevent" #async, gevent,meinheld

from flask import Flask,jsonify
import pymysql
import os


#init
app = Flask(__name__)

#
#
# # connect to db
# conn = pymysql.connect(host='santosrds.mysql.rds.aliyuncs.com', port=3306, user='santosrds', passwd='AAkobe2413', db='dig_goods_db')
# cursor = conn.cursor()
# sql = "select * from t_goods"
# cursor.execute(sql)
# #get result
# result = cursor.fetchall()
# for row in result:
#      print row[4]
# conn.close()

from app import models,views


