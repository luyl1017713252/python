from django.shortcuts import render, HttpResponse


# Create your views here.
from app01.models import User, Role
from rbac.service.rbac import is_permission


def customers(request):
    return HttpResponse('customers...')


def add_customers(request):
    return HttpResponse('add_customers...')


def updatecustomers(request, customer_id):
    return HttpResponse('updatecustomers...')


def delecustomers(request, customer_id):
    return HttpResponse('delecustomers...')


def orders(request):
    return HttpResponse('order...')


def add_order(request):
    return HttpResponse('add_order...')


def updateorder(request, order_id):
    return HttpResponse('updateorder...')


def deleorder(request, order_id):
    return HttpResponse('deleorder...')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=name, pwd=pwd).first()
        if user:
            request.session['user_id'] = user.pk
            is_permission(user, request)
            return HttpResponse('登录成功')

    return render(request, 'login.html')