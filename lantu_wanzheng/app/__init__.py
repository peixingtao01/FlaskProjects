#这个文件存放着app的创建与管理，蓝图的创建
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import pymysql
pymysql.install_as_MySQLdb()
csrfya = CSRFProtect()
models = SQLAlchemy()
def Create_app():
    app = Flask(__name__)
    app.config.from_object('DB_settings.DebugConfig')
    csrfya.init_app(app)
    models.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


