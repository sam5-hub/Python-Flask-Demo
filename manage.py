# __author__ == ''
# -*- coding: utf-8 -*-

# 项目的外部脚本管理文件

from app import app
from flask.ext.script import Manager
from app.models import mysql_db
from playhouse.migrate import *
manager = Manager(app)



@manager.command
def alter_table():
    title_field = CharField(default='')
    status_field = IntegerField(null=True)
    migrator = MySQLMigrator(mysql_db)
    migrate(
        migrator.add_column('User', 'user_id', title_field),
    )



@manager.command
def fetch():
    pass


if __name__ == '__main__':
    manager.run()
