from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import UserInfo

'''
forms组件
    1、校验数据
    2、页面显示提示信息

'''

from django import forms

# class BookFrom(forms.Form):
#     title = forms.CharField(max_length=32)
#     price = forms.IntegerField
#     email = forms.EmailField()
from django.forms import widgets


class UserForm(forms.Form):
    msg = {'required': '该字段不能为空', 'invalid': '邮箱格式不正确'}
    user = forms.CharField(label='用户名',max_length=32, min_length=4, error_messages=msg, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label='密码', error_messages=msg,
                             widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    r_pwd = forms.CharField(label='确认密码', error_messages=msg,
                          widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', error_messages=msg, widget=widgets.EmailInput(attrs={'class': 'form-control'}))

    # 局部钩子 像是陷阱
    def clean_user(self):
        # 拿到客户端传过来的user
        val = self.cleaned_data.get('user')
        # 去数据库钟查找是否有该用户
        ret = UserInfo.objects.filter(user=val)
        if ret:
            # 有的话报一个错误
            raise ValidationError('用户名已存在')
        else:
            # 没有的话就放行
            return val

    def clean_pwd(self):
        # 密码不能为纯数字
        val = self.cleaned_data.get('pwd')
        if val.isdigit():
            raise ValidationError('密码不能为纯数字')
        else:
            return val
    # 全局钩子
    def clean(self):
        # 拿到密码和确认密码
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('密码不一致')





def reg(request):
    if request.method == 'POST':
        # 1、获取页面传递的数据
        # 2、验证是否合规
        form = UserForm(request.POST)
        # 3、合规就插入数据
        if form.is_valid():
            # print(obj.cleaned_data)
            UserInfo.objects.create(**form.cleaned_data)
            return HttpResponse('ok')
        else:
            # 4、不合规把错误信息给页面
            # print(obj.cleaned_data)
            # print(obj.errors)
            print(form.errors.get('email')[0])
            # errors = form.errors
            g_error = form.errors.get('__all__')
        return render(request, 'reg.html', locals())

    else:
        # 用forms渲染页面
        form = UserForm()
        return render(request, 'reg.html', locals())
