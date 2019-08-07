#路由与视图
import hashlib
from flask import render_template,request,redirect,url_for,Response
from setting import app
from models import Student,User

# 加密
def set_mima(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

# 列表
@app.route('/student_list/')
def student_list():
    students = Student.query.all()
    return render_template('students.html',**locals())

# 登录
@app.route('/login/',methods=['POST','GET'])
def login():
    # 设置cookie
    res = render_template('login.html',**locals())
    response = Response(res)
    response.set_cookie('login','login_data')
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
                    reds.set_cookie('username',username)
                    return reds
                else:
                    reds = redirect(url_for('login'))
                    reds.set_cookie('username', '')
                    return reds

        else:
            return '账号密码不可为空'
    return response

# 注册
@app.route('/register/',methods=['POST','GET'])
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
    return render_template('register.html',**locals())

@app.route('/index/')
def index():
    return render_template('index.html',**locals())