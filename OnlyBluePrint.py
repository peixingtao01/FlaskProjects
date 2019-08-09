# 蓝图是一种模板，程序可以生成一段web应用
from flask import Flask
from flask import Blueprint #加载蓝图文件

simple_blueprint = Blueprint('simple_page',__name__) #创建蓝图

@simple_blueprint.route('/')
def index():
    return 'hello world'

# 启动项目
if __name__ == '__main__':
    app = Flask(__name__)#创建一个flask app
    app.register_blueprint(simple_blueprint)#在app内部注册蓝图
    app.run()


