from django.db import models

# Create your models here.
# 创建用户的账号表格
class Account(models.Model):
    account = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50, null=False)

# 定义一个教师表格
class Teacher(models.Model):
    t_id = models.CharField(max_length=10, primary_key=True)
    t_name = models.CharField(max_length=20, null=False)
    t_sex = models.CharField(max_length=10, null=False)
    t_pos = models.CharField(max_length=10)

# 定义一个课程表
class Course(models.Model):
    c_id = models.CharField(max_length=10, primary_key=True)
    c_name = models.CharField(max_length=50, null=False)
    c_tid = models.ManyToManyField(Teacher)
    c_score = models.CharField(max_length=3, null=False)
    c_num = models.IntegerField(default=0)

# 班级表
class Classroom(models.Model):
    r_name = models.CharField(max_length=100, primary_key=True)
    r_num = models.IntegerField(default=0)

# 定义学生表格
class Student(models.Model):
    s_id = models.CharField(max_length=10, primary_key=True)
    s_name = models.CharField(max_length=20, null=False)
    s_sex = models.CharField(max_length=10, null=False)
    s_tel = models.CharField(max_length=11, null=False)
    s_rname = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    s_cid = models.ManyToManyField(Course)

# 定义成绩表
class Score(models.Model):
    c_id = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    s_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)# 学号
    score = models.CharField(max_length=3, null=True)
    c_name = models.CharField(max_length=30)
