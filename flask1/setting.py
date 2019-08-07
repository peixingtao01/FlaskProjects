#此处配置文件，数据库，路径等等
'''
import pymysql#配置musql使用
'''
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASE_DIR,'StudentSYS.sqlite')
# 配置数据连接的参数
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 请求结束后自动提交数据库修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 可以追踪对象的修改并且自动发送信号。但是需要额外内存

"""
app.config.from_object('config.DebugConfig')#连接配置文件
models = SQLAlchemy(app)#连接数据库与项目
