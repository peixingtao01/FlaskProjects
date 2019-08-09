from flask import Flask
from flask_script import Manager

app = Flask(__name__)

@app.route('/')
def index():
    return 'flaskscript_minglinghang'

manage = Manager(app)
@manage.command
def hello(name = 'createsuperuser'):
    # 给命令行增加了一条命令
    input('name:')
    input('password:')
    input('email')
    return '创建成功'

if __name__ =='__main__':
    manage.run()


