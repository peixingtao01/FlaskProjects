'''
将配置文件分开，有配置数据库的文件，有配置app的文件，然后将他们连起来
'''
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 文件绝对路径(本文件所在文件夹)
class BaseConfig(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(24)#加盐

# class DebugConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI =  'mysql://root:123@localhost:3306/school?charset=utf8')

class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'sqlite:///'+os.path.join(BASE_DIR,'StudentSYS.sqlite')

















class OnLineConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI =  'sqlite:///'+os.path.join(BASE_DIR,'Student.sqlite')
