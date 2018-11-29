from django.shortcuts import render, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def show_login(request):
    return render(request, 'app1/login.html')
def show_regist(request):
    return render(request, 'app1/regist.html')
def show_home(request):
    return render(request, 'home/home.html')

# 定义函数完成注册操作
@csrf_exempt
def add_request(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(username) == 0 or len(password) == 0:
            return HttpResponse(json.dumps({'code': 400, 'msg': '账号密码不能为空！'}))
        # 判断该用户是否存在
        if Account.objects.filter(account=username).count() == 0:
            Account.objects.create(account=username, password=password)
            return HttpResponse(json.dumps({'code': 200, 'msg':'注册成功！'}))
        else:
            return HttpResponse(json.dumps({'code': 400, 'msg': '用户名已存在！'}))
    else:
        return HttpResponse(json.dumps({'code': 500, 'msg': '服务器内部错误！'}))

# 定义函数完成登陆
@csrf_exempt
def add_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username)==0 or len(password) == 0:
            return HttpResponse(json.dumps({'code': 400, 'msg': '账号密码不能为空！'}))
        # 判断该用户是否存在
        if Account.objects.filter(account=username, password=password).count() != 0:
            return HttpResponse(json.dumps({'code': 200}))
        else:
            return HttpResponse(json.dumps({'code': 400, 'msg': '登陆失败！'}))


# 定义函数完成班级信息的查找
def get_classes(request):
    # 查询所有的班级信息
    classes = Classroom.objects.all()
    names = [item.r_name for item in classes]
    return HttpResponse(json.dumps(names))

# 定义函数完成学生信息的添加
@csrf_exempt
def add_stuinfor(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        if Student.objects.filter(s_id=s_id).count() == 0:
            name = request.POST.get('name')
            tel = request.POST.get('phone')
            sex = request.POST.get('sex')
            classroom = request.POST.get('class')
            classobj = Classroom.objects.filter(r_name=classroom).first()
            classobj.r_num += 1
            Student.objects.create(s_id=s_id, s_name=name, s_tel=tel, s_sex=sex, s_rname=classobj)
            return HttpResponse(json.dumps({'code': 200, 'msg': '添加成功！'}))
        else:
            return HttpResponse(json.dumps({'code': 400, 'msg': '学生已存在！'}))

    else:
        return HttpResponse(json.dumps({'code': 500, 'msg': '服务器内部错误！'}))


# 定义函数完成课程的添加
@csrf_exempt
def add_scours(request):
    if request.method == 'POST':
        c_id = request.POST.get('c_id')
        if(Course.objects.filter(c_id=c_id).count() == 0):
            teacher = request.POST.get('teacher')
            c_name = request.POST.get('c_name')
            c_course = request.POST.get('c_course')
            c_tid = Teacher.objects.filter(t_id=teacher).first()
            course = Course.objects.create(c_id=c_id, c_name=c_name, c_score=c_course)
            course.c_tid.set([c_tid])
            course.save()
            return HttpResponse(json.dumps({'code':200, 'msg': '课程添加成功！'}))
        else:
            return HttpResponse(json.dumps({'code': 400, 'msg': '课程编号冲突！'}))
    else:
        return HttpResponse(json.dumps({'code': 500, 'msg': '服务器内部错误！'}))

# 获取所有的课程
@csrf_exempt
def get_crouse(request):
    c = Course.objects.all()
    c = [item.c_name for item in c]
    return HttpResponse(json.dumps(c))

# 根据课程名字查询所有的授课老师
def get_all_teachers(request):
    c_name = request.GET.get('c_name')
    # course = Course.objects.filter(c_name=c_name).first()
    course = Course.objects.filter(c_name=c_name).all()
    for i in course:
        teas = [{'id': item.t_id, 'name': item.t_name} for item in i.c_tid.all()]
        return HttpResponse(json.dumps(teas))

# 定义函数完成教师工号的获取
def get_teaid(request):
    teas = Teacher.objects.all()
    t_ids = [item.t_id for item in teas]
    return HttpResponse(json.dumps(t_ids))

# 定义函数建立学生成绩与课程之间的联系
@csrf_exempt
def touch_score(request):
    if request.method=='POST':
        s_id = request.POST.get('s_id')
        if Student.objects.filter(s_id=s_id).count() != 0:
            c_name = request.POST.get('c_name')
            name_id = request.POST.get('t_id')
            if name_id != '请选择':
                result = name_id.split('(')
                t_id = result[1].split(')')[0]
                if Score.objects.filter(s_id__s_id=s_id).count()!=0 and Score.objects.filter(c_id__c_name=c_name).count()!=0:
                    return HttpResponse(json.dumps({'code': 400, 'msg': '此学生已经选过该课！'}))
                else:
                    ccc = Course.objects.filter(c_name=c_name).first()
                    ttt = Student.objects.filter(s_id=s_id).first()
                    Score.objects.create(c_name=c_name, s_id=ttt, c_id=ccc)
                    return HttpResponse(json.dumps({'code': 200, 'msg': '保存成功！'}))
            else:
                return HttpResponse(json.dumps({'code': 400, 'msg': '请选择对应老师！'}))
        else:
            return HttpResponse(json.dumps({'code': 400, 'msg': '此学生不存在！'}))
    else:
        return HttpResponse(json.dumps({'code': 500, 'msg': '服务器内部错误！'}))