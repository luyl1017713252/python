from PIL import Image, ImageDraw, ImageFont
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import random
from rbac.models import UserInfo, Role
from rbac.service.rbac import is_permission


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        res = {'user': None, 'error': ''}
        user_obj = UserInfo.objects.filter(name=username, password=password).first()
        # print(user_obj)
        if user_obj:
            res['user'] = username
            # auth.login(request, user_obj)
            request.session['user_id'] = user_obj.pk
            is_permission(user_obj, request)
        else:
            res['error'] = '用户名密码错误'
        return redirect('/customer/list/')
        # return JsonResponse(res)
    else:
        return render(request, 'login.html')


def get_random_color( ):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def valid_img(request):
    # 方式一 读取一张指定的图片发给浏览器
    # with open('static/img/vaildcode.png', 'rb') as f:
    #     data = f.read()

    # 方式二 基于PIL模块创建图片  pip3 install pillow
    # img = Image.new('RGB', (350, 35), get_random_color())
    # f = open('static/img/valid.png', 'wb')
    # img.save(f, 'png')
    # with open('static/img/valid.png', 'rb') as f:
    #     data = f.read()

    # 方式三 基于PIL模块创建图片  BytesIO 将图片写入内存中
    from io import BytesIO
    img = Image.new('RGB', (350, 35), get_random_color())
    # 方法四 添加文字
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("web/static/font/苹方黑体-中粗-简.ttf", 32)
    # 方式五 文字内容应该是随机产生的
    # 0-9 a-z A-Z 97-122 65-90
    valid_str = ''
    for i in range(4):
        num = str(random.randint(0, 9))
        lowalf = chr(random.randint(97, 122))
        upalf = chr(random.randint(65, 90))
        random_text = random.choice([num, lowalf, upalf])
        draw.text((125 + i * 20, 0), random_text, get_random_color(), font=font)
        valid_str += random_text

    # width = 350
    # height = 38
    # for i in range(8):
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
    img.save(f, 'png')  # 将图片写到内存中
    data = f.getvalue()
    print(valid_str)
    request.session['valid_str'] = valid_str

    return HttpResponse(data)


def logout(request):
    auth.logout(request)
    return redirect('/login/')
