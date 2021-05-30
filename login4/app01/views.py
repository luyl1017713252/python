import re

from django import forms
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.forms import widgets

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from PIL import Image, ImageDraw, ImageFont
import random

# Create your views here.
from app01.models import UserInfo


def login(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_code = request.POST.get('validcode')
        res = {'user': None, 'error': ''}
        print('valid_code', valid_code)
        if valid_code.upper() == request.session.get('valid_str').upper():
            # 1、拿着用户名和密码去数据查
            user_obj = auth.authenticate(username=username, password=password)
            # 2、如果是有用户 返回成功的数据
            if user_obj:
                res['user'] = username
            else:
                res['error'] = '用户名或密码错误'
            # 3、如果没有用户 返回错误信息
            return JsonResponse(res)
        else:
            return HttpResponse('fail')

    else:
        return render(request, 'login.html')


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def valid_img(request):
    # 方式1 读取一张指定图片 发给浏览器
    # with open('static/img/validcode.png', 'rb') as f:
    #     data = f.read()

    # 方式2 基于PIL模块来创建图片  pip3 install pillow
    # img = Image.new('RGB', (350, 35), get_random_color())
    # f = open('static/img/valid.png', 'wb')
    # img.save(f, 'png')
    # with open('static/img/valid.png', 'rb') as f:
    #     data = f.read()

    # 方式3 基于PIL模块来创建图片  BytesIO 将图片写入到内存中
    from io import BytesIO
    img = Image.new('RGB', (350, 35), get_random_color())
    # 方式4 添加文字
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('static/font/苹方黑体-中粗-简.ttf', 28)
    # 方式5 文字内容应该是随机产生的 0 - 9 a - z A - Z 小写 97 - 122  大写 65 - 90
    valid_str = ''
    for i in range(6):
        num = str(random.randint(0, 9))
        lowalf = chr(random.randint(97, 122))
        uperalf = chr(random.randint(65, 90))
        random_char = random.choice([num, lowalf, uperalf])
        draw.text((i * 30 + 100, 0), random_char, get_random_color(), font=font)
        valid_str += random_char

    # width = 350
    # height = 38
    # for i in range(10):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw.line((x1, y1, x2, y2), fill=get_random_color())
    #
    # for i in range(50):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    f = BytesIO()
    img.save(f, 'png')  # 将图片写到内存中了
    data = f.getvalue()
    print(valid_str)
    request.session['valid_str'] = valid_str

    return HttpResponse(data)


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32)
    password = forms.CharField(max_length=32, min_length=8, widget=widgets.PasswordInput())
    r_password = forms.CharField(max_length=32, min_length=8, widget=widgets.PasswordInput())
    email = forms.EmailField(max_length=32, widget=widgets.EmailInput())
    tel = forms.CharField(max_length=32, min_length=11)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        val = self.cleaned_data.get('username')
        user = UserInfo.objects.filter(username=val).first()
        if user:
            raise ValidationError('用户名已存在')
        else:
            return val

    def clean_password(self):
        val = self.cleaned_data.get('password')
        if val.isdigit():
            raise ValidationError('密码不能是纯数字')
        else:
            return val

    def clean(self):
        password = self.cleaned_data.get('password')
        r_password = self.cleaned_data.get('r_password')
        if password == r_password:
            return self.cleaned_data
        else:
            self.add_error('r_password', ValidationError('两次密码不一致!'))

    # def clean_tel(self):
    #     # 拿到tel数据
    #     # 通过正则来匹配tel
    #     # 为true返回tel else raise 报错电话号码格式有误
    #     pass

    def clean_email(self):
        # 拿到email数据
        email = self.cleaned_data.get('email')
        # 通过正则来匹配email
        if re.search('\w+@qq.com$', email):
            # 为true返回tel else raise 报错电话号码格式有误
            return email
        else:
            raise ValidationError('email必须是QQ邮箱')


def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        res = {'user': None, 'err_msg': ''}
        if form.is_valid():
            # 成功 用户信息添加到数据库
            res['user'] = form.cleaned_data.get('username')
            form.cleaned_data.pop('r_password')
            print('clieand_data:', form.cleaned_data)
            UserInfo.objects.create_user(**form.cleaned_data)
        else:
            # 失败 返回错误信息
            res['err_msg'] = form.errors
        return JsonResponse(res)
    else:
        form = UserForm()
        return render(request, 'reg.html', locals())
