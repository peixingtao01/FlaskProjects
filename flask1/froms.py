import wtforms # 定义字段
from flask_wtf import FlaskForm #用于生成表单
from wtforms import validators #定义校验
from models import Course
"""
form字段的参数
label=None, 表单的标签
validators=None, 校验，传入校验的方法
filters=tuple(), 过滤
description='',  描述
id=None, html id
default=None, 默认值
widget=None,
render_kw=None,
"""
course_list = [(C.id,C.lable) for C in Course.query.all()]
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
        # choices=[
        #     ('value1','python'),
        #     ('value2','java'),
        #     ('value3','C'),
        #     ('value4','C++'),
        #     ('value5','C#'),
        # ]
    )

# 这个只会在前端形成一些input表单，像是form框什么的，就不会生成
