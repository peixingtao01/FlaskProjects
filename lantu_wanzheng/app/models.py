from app import models
#设置session是为了对这个数据库进行一些非数据库操作
# 也可以理解为，将这个数据库增加了功能
class Base(models.Model):
    __abstract__ = True
    id = models.Column(models.Integer,primary_key = True,autoincrement=True)
    def saved(self):
        db = models.session()
        db.add(self)
        db.commit()
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


class Attendance(Base):
    # 考勤？？
    __tablename__ = 'attendance'
    att_time = models.Column(models.Date)
    status = models.Column(models.Integer,default=1)
    students_id = models.Column(models.Integer,models.ForeignKey('student.id'))

# models.drop_all()
# models.create_all()
