# 命令行文件
from app import models,Create_app
from flask_script import Manager #增加命令行功能
from flask_migrate import Migrate #同步数据库可用
from flask_migrate import MigrateCommand #同步数据库可用命令行

app = Create_app()

manager = Manager(app)

migrate = Migrate(app,models)#连接数据库与app的,使用的是命令行,同步用

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()


