# __author__ == ''
# -*- coding: utf-8 -*-
# ==========  ===============================================  =============================
# HTTP 方法   URL                                              动作
# ==========  ===============================================  ==============================
# GET         http://[hostname]/todo/api/v1.0/tasks            检索任务列表
# GET         http://[hostname]/todo/api/v1.0/tasks/[task_id]  检索某个任务
# POST        http://[hostname]/todo/api/v1.0/tasks            创建新任务
# PUT         http://[hostname]/todo/api/v1.0/tasks/[task_id]  更新任务
# DELETE      http://[hostname]/todo/api/v1.0/tasks/[task_id]  删除任务
# ==========  ================================================ =============================
import json
from bson import json_util
from app import app
from flask import request,jsonify
from flask.ext.restful import Api,Resource,reqparse
from playhouse.shortcuts import *
from models import *



api = Api(app)


#API

@app.route('/')
def index():
    return '404'

# 取得主题列表
@app.route('/get_topic_list',methods=['GET','POST'])
def get_topic_list():

    list = []
    for topic in t_topic.select():
        list.append(model_to_dict(topic))

    return jsonify({'data':list}),200

# 根据 topic_id 取得主题对应的商品数组
@app.route('/get_topic_detail_goods',methods=['POST','GET'])
def get_topic_detail_goods():

    topic_id = request.values['topic_id']
    goodslist = (t_goods
                .select(t_goods)
                .where(t_goods.topic_id == topic_id)
                .order_by(t_goods.goods_id))

    list = []
    for goods in goodslist:
        list.append(model_to_dict(goods))

    return jsonify({'data':list}),200




# 根据 topic_id 收藏一下
@app.route('/post_topic_like',methods=['POST','GET'])
def post_goods_like():

    topic_id = request.values['topic_id']
    user_id = request.values['user_id']
    like = request.values['like']

    query = (t_user_goods.update(like = like)
                            .where(t_user_goods.topic_id == topic_id & t_user_goods.user_id == user_id))
    query.execute()
    return jsonify({'data':query}),200

#
#
# 根据goods_id收藏一下
@app.route('/post_goods_like',methods=['POST','GET'])
def get_goods():
    goods_id = request.values['goods_id']
    user_id = request.values['user_id']
    like = request.values['like']

    query = (t_user_topic.update(like = like)
                            .where(t_user_topic.goods_id == goods_id & t_user_topic.user_id == user_id))
    query.execute()
    return jsonify({'data':query}),200



# 用户注册
@app.route('/register_user',methods=['POST','GET'])
def get_goods():
    username = request.values['username']
    password = request.values['password']
    user_id = ""

    if t_user.get(t_user.username == username).username:
        return jsonify({'data':"user had exist"})
    else:
        data_dict = {'username':username,'password':password,'user_id' : ''}
        t_user.create(**data_dict)
        return jsonify({'data':data_dict}),200









