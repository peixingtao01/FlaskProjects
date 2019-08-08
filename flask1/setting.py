#此处配置文件，数据库，路径等等
'''
import pymysql#配置musql使用
'''
import os,pymysql
from flask import Flask
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
# pymysql.install_as_MySQLdb()
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASE_DIR,'StudentSYS.sqlite')
# 配置数据连接的参数
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 请求结束后自动提交数据库修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 可以追踪对象的修改并且自动发送信号。但是需要额外内存

"""
csrfya = CSRFProtect(app)
app.config.from_object('config.DebugConfig')#连接配置文件
# app.config['SECRET_KEY'] = os.urandom(24)
models = SQLAlchemy(app)#连接数据库与项目


