#manage.py是启动程序的入口，只关心启动相关参数和内容，不关心业务逻辑
#通过指定的配置名字，创建对应配置的APP

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import create_app,db

app = create_app('development')
#把Manage类与应用实例相关联
manager = Manager(app)

Migrate(app,db)

#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db',MigrateCommand)

if __name__ == 'main':
    manager.run()