import wtforms # 定义字段
from flask_wtf import FlaskForm #用于生成表单
from wtforms import validators #定义校验

course_list =[]
class TeacherFrom(FlaskForm):
    name = wtforms.StringField(
        '教师姓名',
        render_kw={
          'class':'form-control',
          'placeholder':'教师姓名'
        },#属性增加
    )
    age = wtforms.IntegerField(
        '教师年龄',
        render_kw={
            'class': 'form-control',
            'placeholder': '教师姓名'
        },  # 属性增加
    )
    gender = wtforms.StringField(
        '教师性别',
        render_kw={
            'class': 'form-control',
            'placeholder': '教师姓名'
        },  # 属性增加
    )
    course = wtforms.SelectField(
        '学科',
        render_kw={
            'class': 'form-control',
            'placeholder': '教师姓名'
        },  # 属性增加
        choices=course_list
    )

# 这个只会在前端形成一些input表单，像是form框什么的，就不会生成
