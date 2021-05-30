import json
import re

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app01.models import UserInfo


def index(request):
    print(request.method)  # 请求方式
    print(request.path)  # 请求路径
    print(request.POST)  # post请求的数据
    print(request.GET)  # get请求的数据
    # print(request.META)# 消息头
    print(request.get_full_path())  # url全地址
    print(request.is_ajax())  # 是否是一个ajax请求
    '''
    Django 对于响应有一个HttpResponse的实例对象
        1.HttpResponse('字符串')
        2.render('request','页面') 转发  将数据转发给index.html
            控制页面的跳转
            传递变量
        3.redirect() 重定向

    '''
    user = request.COOKIES.get('user')
    is_login = request.COOKIES.get('is_login')
    if not is_login:
        return redirect('/login/')
    # shangpin = '苹果'
    shopping_list = ['苹果', '香蕉', '橘子', '榴莲']
    return render(request, 'index.html', {"sp": shopping_list, 'user': user})
    # return redirect('/index/') 页面最好不能重定向自己本身


def login(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 拿到用户名和密码
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 返回结果
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd)
        if user_obj:
            # 设置cookie HttpResponse
            # HttpResponse.set_cookie('user',user)
            # redirect('/index/')
            print('进入login')
            obj = HttpResponse('OK')
            obj.set_cookie('user', user)
            obj.set_cookie('is_login', True, max_age=3600 * 24, path='/index/')
            return obj  # 重定向去首页
            # shopping_list = ['苹果', '香蕉', '橘子', '榴莲']
            # return render(request, 'index.html',{"sp": shopping_list})
        error = '用户名或者密码错误'
        return render(request, 'login.html', locals())


def login_seesion(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 拿到用户名和密码
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 返回结果
        user_obj = UserInfo.objects.filter(user=user, pwd=pwd)
        if user_obj:
            # 设置seesion
            request.session['username'] = user
            request.session['is_login'] = True
            ''' 

                if  request.Cookie.get('sessionId'): 判断有没有sessionId
                    sessionId = request.Cookie.get('sessionId')
                    filter('session_key' = sessionId)
                    1、django 生成了一个随机的字符串 x80m7db2y4e8xjulq7ph6i5nc33tmn39
                    2、向django_session表update
                        seesion-key                        session-data
                        x80m7db2y4e8xjulq7ph6i5nc33tmn39  eyJ1c2VybmFtZSI6InRvbXR1IiwiaXNfbG9naW4iOnRydWV9
                    3、响应 set_cookie {'seesionid':x80m7db2y4e8xjulq7ph6i5nc33tmn39}
                else:  
                    1、django 生成了一个随机的字符串 x80m7db2y4e8xjulq7ph6i5nc33tmn39
                    2、向django_session表插入记录
                        seesion-key                        session-data
                        x80m7db2y4e8xjulq7ph6i5nc33tmn39  eyJ1c2VybmFtZSI6InRvbXR1IiwiaXNfbG9naW4iOnRydWV9
                    3、响应 set_cookie {'seesionid':x80m7db2y4e8xjulq7ph6i5nc33tmn39}

            '''

            return redirect('/index_seesion/')
            # shopping_list = ['苹果', '香蕉', '橘子', '榴莲']
            # return render(request, 'index.html',{"sp": shopping_list})
        # error = '用户名或者密码错误'
        return render(request, 'login.html', locals())


def index_seesion(request):
    print(request.session)
    is_login = request.session.get('is_login')
    '''
        1、requeset.Cookie.get('seesionid') x80m7db2y4e8xjulq7ph6i5nc33tmn39
        2、在django_session表过滤filter取出来data  eyJ1c2VybmFtZSI6InRvbXR1IiwiaXNfbG9naW4iOnRydWV9
        3、将DATA反序列化回{'username':tomtu,'is_login':True}
    '''
    if not is_login:
        return redirect('/login_seesion/')
    user = request.session.get('username')
    print(user)
    # shangpin = '苹果'
    shopping_list = ['苹果', '香蕉', '橘子', '榴莲']
    return render(request, 'index.html', {"sp": shopping_list, 'user': user})
    # return redirect('/index/') 页面最好不能重定向自己本身


def logout(request):
    # 删除session
    '''
        1.request.Cookie.get('sessionId')
        2.filter(session_key='12he1h2euhuid').del()
        3.response.delete_cookie('sessionId')
    '''
    request.session.flush()
    return redirect('/login_seesion/')


def register(request):
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    user_pwd_dict = {'user': user, 'pwd': pwd}
    ret = UserInfo.objects.create(user=user, pwd=pwd)
    if ret:
        return HttpResponse(json.dumps(user_pwd_dict))
    else:
        return HttpResponse('no')
