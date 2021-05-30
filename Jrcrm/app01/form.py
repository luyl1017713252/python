import random
import re

from django.forms import widgets as wid
from django.contrib import auth
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from PIL import Image, ImageDraw, ImageFont

# Create your views here.
from multiselectfield import MultiSelectFormField

from app01.models import UserInfo, ConsultRecord, Customer, Enrollment, PaymentRecord, StudentStudyRecord, Permission, \
    Student, ClassStudyRecord, Role


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='性别', choices=((1, '男'), (2, '女')))
    password = forms.CharField(label='密码', max_length=32, min_length=3, widget=widgets.PasswordInput())
    r_password = forms.CharField(label='确认密码', max_length=32, min_length=3, widget=widgets.PasswordInput())
    email = forms.EmailField(label='邮箱', max_length=32, widget=widgets.EmailInput())
    tel = forms.CharField(label='电话', max_length=32, min_length=11)

    def __init__(self, *args, **kwargs):
        # 调用父类的
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class from-conto..
        # 先拿到所有的field
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        val = self.cleaned_data.get('username')
        user = UserInfo.objects.filter(username=val).first()
        if user:
            raise ValidationError('用户名已经存在')
        else:
            return val

    # def clean_password(self):
    #     val = self.cleaned_data.get('password')
    #     if val.isdigit():
    #         raise ValidationError('密码不能是纯数字')
    #     else:
    #         return val

    # 全局钩子
    def clean(self):
        # 拿到密码和确认密码
        password = self.cleaned_data.get('password')
        r_password = self.cleaned_data.get('r_password')
        if password == r_password:
            return self.cleaned_data
        else:
            self.add_error('r_password', ValidationError('两次密码不一样'))

    def clean_tel(self):
        # 拿到tel数据
        tel = self.cleaned_data.get('tel')
        # 通过正则来匹配tel
        if re.search('\d+', tel):
            return tel
        else:
            raise ValidationError('电话格式有误')
        # 为true返回tel else raise 报错电话号码格式有误

    def clean_email(self):
        # 拿到email数据
        email = self.cleaned_data.get('email')
        # 通过正则来匹配email
        if re.search('\w+@qq.com$', email):
            return email
        else:
            raise ValidationError('email格式有误')


class CustomersModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'birthday': wid.TextInput(attrs={'type': 'date'}),
            'next_date': wid.TextInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            if isinstance(field, MultiSelectFormField):
                continue
            field.widget.attrs.update({'class': 'form-control'})


class ConsultRecordsForm(forms.ModelForm):
    class Meta:
        model = ConsultRecord
        exclude = ['delete_status']
        widgets = {
            'date': wid.TextInput(attrs={'type': 'date'})
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        self.fields['consultant'].queryset = UserInfo.objects.filter(pk=request.user.pk)
        self.fields['customer'].queryset = Customer.objects.filter(consultant=request.user.pk)
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        exclude = ['delete_status']
        # widgets = {
        #     'date': wid.TextInput(attrs={'type': 'date'})
        # }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        self.fields['customer'].queryset = Customer.objects.filter(consultant=request.user.pk)
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class PaymentRecordModelForm(forms.ModelForm):
    class Meta:
        model = PaymentRecord
        exclude = ['delete_status']
        widgets = {
            'confirm_date': wid.TextInput(attrs={'type': 'date'})
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        print(request.user.pk)
        self.fields['confirm_user'].queryset = UserInfo.objects.filter(pk=request.user.pk)
        self.fields['customer'].queryset = Customer.objects.filter(consultant=request.user.pk)
        self.fields['consultant'].queryset = UserInfo.objects.filter(departments=1, username=request.session['username'])
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class PersonalDataModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'tel', 'gender', 'email']
        labels = {
            'username': '用户名',
            'gender': '性别',
            'email': '邮箱',
            'tel': '电话',
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class PermissionModelForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['customer', 'emergency_contract']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        if not re.search(r'/student/edit/(\d+)/', request.path):
            student_list = list(Student.objects.all().values('customer'))
            customer = [i['customer'] for i in student_list]
            customer_list = Customer.objects.exclude(id__in=customer)
            self.fields['customer'].queryset = customer_list
        for field in self.fields.values():
            # print(self.errors.get('required'))

            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class ClassstudyRecordModelForm(forms.ModelForm):
    class Meta:
        model = ClassStudyRecord
        fields = '__all__'


    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = UserInfo.objects.filter(roles=6)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})


class RoleModelForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})

class UserInfoModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'gender', 'tel', 'email', 'roles', 'departments']
        labels = {
            'username': '用户名',
            'tel': '电话',
            'gender': '性别',
            'roles': '角色',
            'departments': '部门',
            'email': '邮箱'
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 拿到所有的字段对象 给他们加上class form-con...
        # 先拿到所有fields   公用的资源修改方式
        for field in self.fields.values():
            # print(self.errors.get('required'))
            field.error_messages = {'required': '不能为空'}
            field.widget.attrs.update({'class': 'form-control'})