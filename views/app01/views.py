from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 拿到用户名和密码
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 返回结果
        if user == 'Tomtu' and pwd == '123':
            return redirect(reverse('index2'))# 重定向去首页
        return HttpResponse('fail')


def index(request):
    print(request.method)# 请求方式
    print(request.path)# 请求路径
    print(request.POST)# post请求的数据
    print(request.GET) # get请求的数据
    # print(request.META) # 消息头
    print(request.get_full_path())# url全地址
    print(request.is_ajax())# 是否是一个ajax请求
    '''
    Django 对于响应有一个HttpResponse的实例对象
        1.HttpResponse('字符串')
        2.render('request', '页面')
            控制页面的跳转
            传递变量
        3.redirect() 重定向
    '''
    shangpin = '苹果'
    shopoing_list = ['苹果', '香蕉', '橘子', '榴莲']
    return render(request, 'index.html', {"sp": shopoing_list})
    # return redirect('/index/') # 页面最好不要重定向本身