'''
管理项目文件
'''
from models import models
from views import app

if __name__=='__main__':
    models.create_all()
    app.run()

