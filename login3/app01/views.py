from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth

# Create your views here.
def reg(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    else:
        # 获取页面传过来的数据
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 插入数据库 auth模块
        User.objects.create_user(username=user, password=pwd)
        return redirect('/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 获取页面传过来的数据
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 去数据库查询又没有该用户

        # authenticate 查询auth——user对象记录，查询成功返回user对象， 失败返回none
        user_obj = auth.authenticate(username=user, password=pwd)
        if user_obj:
            # 保存用户状态信息
            auth.login(request, user_obj)
            return redirect('/index/')
        else:
            return redirect('/login/')

# @login_requi
def index(reqeust):
    print('user', reqeust.user)
    # if not reqeust.user.is_authenticated:
    #     return redirect('/login/')
    name = reqeust.user.username
    return render(reqeust, 'index.html', {'name': name})


def logout(request):
    auth.logout(request)
    return redirect('/login/')


def update(request):
    obj = User.objects.get(username=request.user.username)
    obj.set_password(raw_password='666')
    obj.save()
    return redirect('/login/')