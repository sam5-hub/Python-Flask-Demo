# __author__ == ''
# -*- coding: utf-8 -*-

# 项目的
from peewee import *


mysql_db = MySQLDatabase(host = 'santosrds.mysql.rds.aliyuncs.com', user = 'santosrds',
                         passwd = 'AAkobe2413', database = 'dig_goods_db', charset = 'utf8',threadlocals=True)



class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class t_user(BaseModel):
    id = IntegerField(primary_key = True)
    user_id = CharField(unique=True)
    username = CharField()
    email = CharField()
    token = CharField()
    img_url = CharField()


# User.drop_table(True)

# 专题数据模型
class t_topic(BaseModel):
    __tablename__ = 't_topic'
    ID = IntegerField(primary_key = True)
    topic_id = CharField()
    title = CharField()
    time = TimeField()
    detail = TextField()
    img_url = CharField()

# 商品数据模型
class t_goods(BaseModel):
    __tablename__ = 't_goods'
    ID = IntegerField(primary_key = True)
    goods_id = CharField()
    topic_id = CharField()
    taobao_id = CharField()
    shop_id = CharField()
    taobao_url = CharField()
    time = TimeField()
    data = TextField()

# 商品内容数据模型
class Goods_data(BaseModel):
    __tablename__ = 't_goods_data'
    ID = IntegerField(primary_key = True)
    goods_data_id = CharField()
    data = CharField()
    type = IntegerField()
    time = TimeField()

#     # 0.title
#     # 1.detail
#     # 2.img
#     # 3.des 如果是des的时候 ,data写法是:{"title":材料,"detail":"100%纯棉"}
#     # 4.price
#     # 5.guide_line

# 用户跟商品的关系表
class t_user_goods(BaseModel):

    ID = IntegerField(primary_key = True)
    user_id = CharField()
    goods_id = CharField()
    like = CharField()
    time = TimeField()
#
class t_user_topic(BaseModel):

    ID = IntegerField(primary_key = True)
    user_id = CharField()
    topic_id = CharField()
    like = CharField()
    time = TimeField()