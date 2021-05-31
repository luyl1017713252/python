from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django import forms
# from app01.models import UserInfo
from app01.models import UserInfo


# 首页
def index(request):
    # 判断是否已经登录
    if request.session.get('user'):
        # 如果登入了可以直接去首页
        return render(request, 'index.html')
    else:
        # 如果没登陆，重定向到登录
        return redirect('/login/')


# 登入
class LoginView(View):
    def get(self, request):
        # 返回登录页面
        return render(request, 'login.html')

    def post(self, request):

        # 拿到用户名、密码
        username = request.POST.get('user')
        passwd = request.POST.get('passwd')

        res = {'login_succeed': False, 'login_hint': ''}
        # 到数据库判断有没有这个用户
        user_obj = UserInfo.objects.filter(username=username, password=passwd)

        # 如果有保存session
        if user_obj:
            res['login_succeed'] = True
            request.session['user'] = username
        else:
            res['login_hint'] = '用户名或密码错误'
        return JsonResponse(res)


# 注册
def reg(request):
    username = request.POST.get('user')
    passwd = request.POST.get('passwd')
    passwd2 = request.POST.get('passwd2')
    res = {'reg_succeed': False, 'reg_hint': ''}
    print(username, passwd, passwd2)
    if passwd == passwd2:
        if len(passwd) < 6:
            res['reg_hint'] = '密码不能少于六位数'
        else:
            user_obj = UserInfo.objects.filter(username=username).first()
            if user_obj:
                res['reg_hint'] = '该用户名已被注册'
            else:
                res['reg_succeed'] = True
                res['reg_hint'] = '注册成功'

                UserInfo.objects.create(username=username, password=passwd)
    else:
        res['reg_hint'] = '两次输入密码不一致'

    return JsonResponse(res)


def logout(request):
    del request.session['user']
    return redirect('/login/')


def photo_album(request):

    return render(request,'photo_album.html')

def home(request):

    return render(request, 'home.html')


class Hobby(View):
    def get(self, request):
        return render(request, 'hobby.html')


class Admirer(View):
    def get(self, request):
        return render(request, 'admirer.html')


class ReadingMatter(View):
    def get(self, request):
        return render(request, 'readingmatter.html')


def school(request):
    return render(request,'school.html')