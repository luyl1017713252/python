import json
import os

from django.shortcuts import render, HttpResponse

# Create your views here.
from ajax1907.settings import BASE_DIR
from app01.models import UserInfo


def index(request):
    return render(request, 'index.html')

def handle_ajax(request):
    return HttpResponse('成功发送')

def cal(request):
    # num1 = request.GET.get('num1')
    # num2 = request.GET.get('num2')

    num1 = request.POST.get('num1')
    num2 = request.POST.get('num2')
    # csrf = request.POST.get('csrfmiddlewaretoken')
    num3 = int(num1)+int(num2)
    json_dict = json.loads(request.body.decode('utf-8'))
    return HttpResponse('str(num3)')

def login(request):
    import json
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ret = {'user': None, 'error': ''}
        user = UserInfo.objects.filter(user=user, pwd=pwd).first()
        if user:
            ret['user'] = user.user
        else:
            ret['error'] = '用户名或密码错误'
        return HttpResponse(json.dumps(ret))

    else:
        return render(request, 'login.html')

def file_put(request):
    file_obj = request.FILES.get('file_obj')
    path = os.path.join(BASE_DIR, 'file_put', 'img', file_obj.name)
    with open(path, 'wb') as f:
        for line in file_obj:
            f.write(line)
    return HttpResponse('ok')
