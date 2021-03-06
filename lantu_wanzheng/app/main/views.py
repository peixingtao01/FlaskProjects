#路由与视图
import hashlib,os
from flask import jsonify
from flask import render_template,request,redirect,url_for,Response
from . import main
from app import Create_app
from app.models import Student,User
from app import csrfya
# 加密
from DB_settings import BaseConfig
def set_mima(password):
    # password += BaseConfig.SECRET_KEY #淡了，加盐
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()


# 列表
@main.route('/student_list/')
def student():
    return '这是没有HTML文件的student_list'
# def student_list():
#     students = Student.query.all()
#     return render_template('/tempaltes/students.html',**locals())

@main.route('/userValid/',methods=['POST',"GET"])
def userValid():
    result={'code':'','data':''}
    data = request.args.get('username')
    print(data)
    if data:
        user = User.query.filter_by(username=data).first()
        if user:
            result['code'] = 400
            result['data'] = '用户名已经存在'
        else:
            result['code'] = 200
            result['data'] = '用户名已经注册'
    return jsonify(result)

# 登录
@main.route('/login/',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        psd = request.form['password']
        print(type(psd))
        if username and psd:
            user = User.query.filter_by(username=username).first()
            if username == user.username:
                password = set_mima(psd)
                if password == user.password:
                    reds = redirect(url_for('index'))
                    reds.set_cookie('username',username) # 设置cookie
                    reds.set_cookie('user_id',str(user.id))
                    # session['username'] = username #设置session
                    return reds
                else:
                    reds = redirect(url_for('login'))
                    reds.set_cookie('username', '')
                    return reds
        else:
            return '账号密码不可为空'
    return render_template('login.html',**locals())


# 注册
@main.route('/register/',methods=['POST','GET'])
def register():
    if request.method =='POST':
        # request.form.get("username")
        # 前端获得是用位置取，所以可能是form什么的
        # 后端是直接给了一个类似字典的东西，是直接获取了数据
        username = request.form['username']
        psd = request.form['password']
        if username:
            password = set_mima(psd)
            user = User()
            user.username = username
            user.password = password
            user.saved()
            return redirect(url_for('login'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html',**locals())#直接写返回的前端文件就可以了

@main.route('/index/')
def index():
    username = request.cookies.get('username')
    # user = session.get('username')
    # print(username,user)
    return render_template('index.html',**locals())


# 表单
from app.main.forms import TeacherFrom
@csrfya.exempt
@main.route('/froms/',methods=['POST','GET'])
def froms():
    teacherfrom = TeacherFrom()
    return render_template('fromes.html',**locals())


# @csrfya.error_handler
@main.route('/csrf_403/')
def csrf_403(response):
    print(response)
    return render_template('csrf_403.html',**locals())