from setting import models
session = models.session()#设置session是为了对这个数据库进行一些非数据库操作
# 也可以理解为，将这个数据库增加了功能
class Base(models.Model):
    __abstract__ = True
    id = models.Column(models.Integer,primary_key = True,autoincrement=True)
    def saved(self):
        session.add(self)
        session.commit()
Stu_Cou = models.Table(
    'stu_cou',
    models.Column('id',models.Integer,primary_key=True,autoincrement=True),
    models.Column('course_id',models.Integer,models.ForeignKey('course.id')),
    models.Column('student_id',models.Integer,models.ForeignKey('student.id'))
)
class Student(models.Model):
    __tablename__ = 'student'
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    name = models.Column(models.String(32),unique=True)
    age = models.Column(models.Integer,unique=True)
    gender = models.Column(models.Integer)#成绩
class Course(Base):
    __tablename__ = 'course'
    lable = models.Column(models.String(32),unique=True)
    teachers = models.relationship('Teachers',backref='to_course')
    # 外表用这个字段，本表用backref
    to_student = models.relationship(
        'Student',
        secondary = Stu_Cou,#指向多对多表
        backref = models.backref('to_course_ya',lazy = 'dynamic'),
        lazy = 'dynamic'#不加载数据
    )
class Teachers(Base):
    __tablename__ = 'teachers'
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer)
    cousers_id = models.Column(models.Integer,models.ForeignKey('course.id'))

class User(Base):
    __tablename__='user'
    username = models.Column(models.String(32))
    password = models.Column(models.String(32))

"""
class Stu_Cou(Base):#如果前面有人用了relationship，那么这个多对多关联表就不可以用class进行创建了
    __tablename__ = 'stu_cou'
    cou_id = models.Column(models.Integer,models.ForeignKey('course.id'))
    stu_id = models.Column(models.Integer,models.ForeignKey('student.id'))
"""
# 此时实表应该换成虚表
# t = Teachers.query.get(1)
# c = Course.query.get(1)
# print(t.to_course)
# print(c.teachers)
class Attendance(Base):
    # 考勤？？
    __tablename__ = 'attendance'
    att_time = models.Column(models.Date)
    status = models.Column(models.Integer,default=1)
    students_id = models.Column(models.Integer,models.ForeignKey('student.id'))

# models.drop_all()
# models.create_all()



# ---------------------------------------------------------
"""
# 增--三种方式
t = Teachers(name='zs' ,age=11, gender=1,cousers_id=1)#单这样保存不上
session.add(t)#方式一

teacher = Teachers()
teacher.name = 'ls'
teacher.age = 12
teacher.gender = 2
teacher.cousers_id = 1#方式二

x1 = {'name':'ww','age':13,'gender':1,'cousers_id':1}
X= Teachers(**x1)#方式三

session.add_all([teacher,X])
session.commit()
"""
# ---------------------------------------------------------

# ---------------------------------------------------------
# 改
"""
t = Teachers.query.get(1)
print(t)#<Teachers 1>
t.name = '张三'
session.add(t)
session.commit()
"""
# ---------------------------------------------------------

# ---------------------------------------------------------
# 查，是最多，最繁琐的
"""
v1 = Teachers.query.all()
print(v1)
v2 = Teachers.query.first()
print(v2,v2.name)
v3 = Teachers.query.filter_by(age=11).all()#加上all就不错了，奇怪
print(v3)
v4 = Teachers.query.order_by('age').all()
print(v4)
v5 = Teachers.query.order_by(models.desc('age')).all()
print(v5)
v6 = Teachers.query.get(3)
print(v6)
v7 = Teachers.query.offset(1).limit(3).all
print(v7)
"""
# ---------------------------------------------------------


# ---------------------------------------------------------
# 删
"""
t = Teachers.query.get(2)
session.delete(t)
session.commit()
"""
# ---------------------------------------------------------
'''
c=Course(lable='python',)
session.add(c)
session.commit()
'''
