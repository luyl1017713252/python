import random
import re
import time
import datetime

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth
from django import forms
from django.db.models import Q, Count
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from PIL import Image, ImageDraw, ImageFont

# Create your views here.
from django.urls import reverse
from django.views import View
from multiselectfield import MultiSelectFormField

from app01.models import UserInfo, Customer, ConsultRecord, Enrollment, PaymentRecord, Role, ClassStudyRecord, Student, \
    StudentStudyRecord, Permission, ClassList
from app01.form import UserForm, CustomersModelForm, ConsultRecordsForm, EnrollmentForm, PaymentRecordModelForm, \
    PersonalDataModelForm, PermissionModelForm, StudentModelForm, ClassstudyRecordModelForm, RoleModelForm, \
    UserInfoModelForm
from app01.page import Pagination
from app01.utise.rbac import is_permission


def login(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        validcode = request.POST.get('validcode')
        res = {'user': None, 'error': ''}
        if validcode.upper() == request.session.get('valid_str').upper():
            # 1、去数据库查用户名和密码
            user_obj = auth.authenticate(username=username, password=password)
            # 2、有 返回成功的数据
            if user_obj:
                res['user'] = username
                auth.login(request, user_obj)
                request.session['user_id'] = user_obj.pk
                request.session['username'] = user_obj.username
                is_permission(user_obj, request)
                # permissions_list = []
                # ret = Role.objects.filter(userinfo=user_obj).values('permissions__url').distinct()
                # for i in ret:
                #     permissions_list.append(i['permissions__url'])
                # request.session['permissions_list'] = permissions_list
                # print(request.session['permissions_list'])
            else:
                res['error'] = '用户名或密码错误'
            # 3、无 返回错误信息
            return JsonResponse(res)
        else:
            return HttpResponse('False！')


    else:
        return render(request, 'login.html')


def Search(request):
    val = request.GET.get('text')
    permission_list = request.session['permissions_list']
    show_permission_list = []
    permission_html = '<li class="header">HEADER</li>'
    for item in permission_list:
        if not item['pid']:
            ret = re.search(val, item['title'])
            if ret:
                show_permission_list.append(item)
    print(show_permission_list)

    for i in show_permission_list:
        # '<li><a href="%s" ><i class ="fa fa-link"></i><span>%s</span></a></li>'%(i['url'], i['title'])
        permission_html_one = '<li><a href="%s"><i class ="fa fa-link"></i><span>%s</span></a></li>' % (i['url'], i['title'])
        permission_html += permission_html_one
    return HttpResponse(permission_html)


def get_random_color():
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
    font = ImageFont.truetype('static/font/ARIALUNI.TTF', 32)
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


def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        res = {'user': None, 'err_msg': ''}
        if form.is_valid():
            # 成功将用户信息添加到数据库
            res['user'] = form.cleaned_data.get('username')
            form.cleaned_data.pop('r_password')
            UserInfo.objects.create_user(**form.cleaned_data)
        else:
            # 失败 返回错误信息
            res['err_msg'] = form.errors
        return JsonResponse(res)

    else:
        form = UserForm
        return render(request, 'reg.html', locals())


# def loginver(fn):
#     def inner(request, *args, **kwargs):
#         if request.user.id:
#             return fn(request)
#         else:
#             return redirect('/login/')
#     return inner


@login_required
def index(request):
    result = {}
    ret = UserInfo.objects.all().annotate(
        c=Count('roles')).values_list(
        'roles__title', 'c')
    ret = [item[0] for item in ret]
    for i in set(ret):
        result[i] = ret.count(i)
    ret = [[title, values] for title, values in result.items()]
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {'ret': ret, 'today': today})


class Customers(View):
    def get(self, request):
        val = request.GET.get('q')
        opt = request.GET.get('opt')
        opt = str(opt) + '__contains'
        # 使用reverse判断name反射的path路径，是否等于当前请求的路径
        current_page = request.GET.get('page', '1')
        if reverse('customers_list') == request.path:
            customers_label = '全部客户'
            customers_list = Customer.objects.filter(consultant__isnull=True)
            base_url = 'http://localhost:8000/customers/list'
        elif reverse('mycustomers') == request.path:
            customers_label = '我的客户'
            consultant = request.user
            customers_list = Customer.objects.filter(consultant=consultant)
            base_url = 'http://localhost:8000/mycustomers'
        if val:
            q = Q()
            q.children.append((opt, val))
            customers_list = customers_list.filter(q)
        pagination = Pagination(current_page, customers_list.count(), request, base_url, 2)
        customers_list = customers_list[pagination.start: pagination.end]
        next = '?next=%s' % request.path
        return render(request, 'customers_list.html',
                      {'customers_list': customers_list, 'pagination': pagination, 'customers_label': customers_label,
                       'next': next})

    def post(self, request):
        action = request.POST.get('action')
        pk_list = request.POST.getlist('pk_list')
        print(action)
        if not hasattr(self, action):
            return HttpResponse('非法输入')
        else:
            queset = Customer.objects.filter(pk__in=pk_list)
            func = getattr(self, action)
            res = func(request, queset)
            if res:
                return res
            ret = self.get(request)
            return ret

    def batch_delete(self, request, queset):
        queset.delete()

    def batch_reveres(self, request, queset):
        '''
        公户转私户
        :param request:
        :param queset: 当前选中的客户
        :return:
        '''
        ret = queset.filter(consultant__isnull=True)
        if ret:
            ret.update(consultant=request.user.id)
        else:
            return HttpResponse('手速不够，还得练练')

    def batch_reveres_gh(self, request, queset):
        '''
        私户转公户
        :param request:
        :param queset: 当前选中的客户
        :return:
        '''
        queset.update(consultant=None)


class DeleCustomers(View):
    def get(self, request, id):
        Customer.objects.filter(pk=id).delete()
        return redirect(request.GET.get('next'))


class AddUpdateCustomersView(View):
    def get(self, request, id=None):
        ret = Customer.objects.filter(pk=id).first()
        form = CustomersModelForm(instance=ret)
        return render(request, 'addupdatecustomer.html', {'form': form, 'ret': ret})

    def post(self, request, id=None):
        ret = Customer.objects.filter(pk=id).first()
        form = CustomersModelForm(request.POST, instance=ret)
        # 如果为true 表单的数据插入到数据库中
        if form.is_valid():
            form.save()
            if request.GET.get('next'):
                print('next')
                return redirect(request.GET.get('next'))
            else:
                print('我的')
                return redirect('/mycustomers/')
            # 如果为false 错误信息显示到页面 modelform.error.0
        else:
            return render(request, 'addupdatecustomer.html', {'form': form})


class ConsultRecords(View):
    def get(self, request):
        customer_id = request.GET.get('customers_id')
        current_page = request.GET.get('page', '1')
        print(customer_id)
        consultrecord_label = '跟进记录'
        if reverse('consultrecord') == request.path:
            content_btn_name = '删除'
            consultrecords_list = ConsultRecord.objects.filter(delete_status=False, consultant=request.user)
        elif reverse('reconsultrecord') == request.path:
            content_btn_name = '恢复'
            consultrecords_list = ConsultRecord.objects.filter(delete_status=True, consultant=request.user)
        if customer_id:
            consultrecords_list = consultrecords_list.filter(customer_id=customer_id)
        base_url = 'http://localhost:8000/consultRecord/list'
        pagination = Pagination(current_page, consultrecords_list.count(), request, base_url, 2)
        consultrecords_list = consultrecords_list[pagination.start: pagination.end]
        return render(request, 'consultrecord_list.html',
                      {'consultrecords_list': consultrecords_list, 'content_btn_name': content_btn_name,
                       'pagination': pagination, 'consultrecord_label': consultrecord_label})


class AddConsultRecords(View):
    def get(self, request):
        form = ConsultRecordsForm(request)
        return render(request, 'add_consultrecord.html', {'form': form})

    def post(self, request):
        form = ConsultRecordsForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/consultRecord/list/')
        else:
            return render(request, 'add_consultrecord.html', {'form': form})


class DeleConsultRecords(View):
    def get(self, request, consultrecord_id):
        ret = ConsultRecord.objects.filter(pk=consultrecord_id).values('delete_status')[0]
        if ret['delete_status']:
            ret = ConsultRecord.objects.filter(pk=consultrecord_id).update(delete_status=False)
            return redirect('/re_consultRecord/')
        else:
            ret = ConsultRecord.objects.filter(pk=consultrecord_id).update(delete_status=True)
            return redirect('/consultRecord/list/')



class PaymentRecordView(View):
    def get(self, request):
        customers_label = '缴费记录'
        paymentrecord_list = PaymentRecord.objects.filter(delete_status=False)
        return render(request, 'paymentrecord_list.html',
                      {'paymentrecord_list': paymentrecord_list, 'customers_label': customers_label})


class AddPaymentRecord(View):
    def get(self, request):
        form = PaymentRecordModelForm(request)
        return render(request, 'add_paymentrecord.html', {'form': form})

    def post(self, request):
        form = PaymentRecordModelForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paymentrecord/list/')
        else:
            return render(request, 'add_paymentrecord.html', {'form': form})


class DelePaymentRecord(View):
    def get(self, request, paymentrecord_id):
        PaymentRecord.objects.filter(pk=paymentrecord_id).update(delete_status=True)
        return redirect('/paymentrecord/list/')


class UpdatePaymentRecord(View):
    def get(self, request, id):
        # 返回添加页面 modelform
        ret = PaymentRecord.objects.get(pk=id)
        form = PaymentRecordModelForm(request, instance=ret)
        return render(request, 'updatepaymentrecord.html', {'form': form})

    def post(self, request, id):
        # modelform 表单验证
        ret = PaymentRecord.objects.get(pk=id)
        form = PaymentRecordModelForm(request, request.POST, instance=ret)
        print(request.POST)
        # 如果为true 表单的数据插入到数据库中
        if form.is_valid():
            form.save()
            return redirect('/paymentrecord/list/')
        # 如果为false 错误信息显示到页面 modelform.error.0
        else:
            return render(request, 'updatepaymentrecord.html', {'form': form})


class ClassStudyRecords(View):
    def get(self, request):
        customers_label = '班级信息'
        classstudyrecord_list = ClassStudyRecord.objects.all()
        return render(request, 'classstudyrecord_list.html',
                      {'classstudyrecord_list': classstudyrecord_list, 'customers_label': customers_label})

    def post(self, request):
        action = request.POST.get('action')
        selected_pk_list = request.POST.getlist('pk_list')
        if hasattr(self, action):
            ret = getattr(self, action)(selected_pk_list)
        return self.get(request)

    def batch_init(self, selected_pk_list):
        try:
            for selected_pk in selected_pk_list:
                classstudyrecord_obj = ClassStudyRecord.objects.filter(pk=selected_pk).first()
                students_list = classstudyrecord_obj.class_obj.students.all()
            for student in students_list:
                ret = StudentStudyRecord.objects.filter(student=student)
                print(ret)
                if not ret:
                    StudentStudyRecord.objects.create(student=student, classstudyrecord=classstudyrecord_obj)
        except Exception as e:
            pass

    def batch_delete(self, selected_pk_list):
        for selected_pk in selected_pk_list:
            ClassStudyRecord.objects.filter(pk=selected_pk).delete()



class AddClassstudyRecord(View):
    def get(self, request):
        form = ClassstudyRecordModelForm(request)
        return render(request, 'add_classstudyrecord.html', {'form': form})

    def post(self, request):
        form = ClassstudyRecordModelForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/classstudyrecord/list/')
        else:
            return render(request, 'add_classstudyrecord.html', {'form': form})


class RecordScoreView(View):
    def get(self, request, class_study_record_id):
        class_study_record = ClassStudyRecord.objects.get(pk=class_study_record_id)
        student_study_record_list = class_study_record.studentstudyrecord_set.all()
        score_choices = StudentStudyRecord.score_choices
        return render(request, 'record_score.html', locals())

    def post(self, request, class_study_record_id):
        date_dict = {}
        for key, val in request.POST.items():
            if key == 'csrfmiddlewaretoken':
                continue
            filed, pk = key.rsplit('_', 1)
            if pk not in date_dict:
                date_dict[pk] = {
                    filed: val
                }
            else:
                date_dict[pk][filed] = val
        for pk, data in date_dict.items():
            StudentStudyRecord.objects.filter(pk=pk).update(**data)
        return self.get(request, class_study_record_id)


class DealInfo(View):
    def get(self, request):
        today = datetime.datetime.now().date()
        date = request.GET.get('date', 'today')
        if hasattr(self, date):
            ret = getattr(self, date)()
        return render(request, 'deal_list.html',ret )

    def post(self, request):
        pass

    def get_userinfo_data(self, before_date=None, date=datetime.datetime.now().date()):
        if not before_date:
            ret = UserInfo.objects.filter(departments_id=1, customers__deal_date=date).annotate(
                c=Count('customers')).values_list(
                'username', 'c')
        else:
            ret = UserInfo.objects.filter(departments_id=1, customers__deal_date__gte=before_date,
                                          customers__deal_date__lte=date).annotate(
                c=Count('customers')).values_list(
                'username', 'c')
        ret = [[item[0], item[1]] for item in ret]
        return ret


    def today(self):
        today = datetime.datetime.now().date()
        customer_list = Customer.objects.filter(deal_date=today)
        ret = getattr(self, 'get_userinfo_data')(today)
        return {'customer_list': customer_list, 'ret': ret}

    def yesterday(self):
        yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
        customer_list = Customer.objects.filter(deal_date=yesterday)
        ret = getattr(self, 'get_userinfo_data')(yesterday)
        return {'customer_list': customer_list, 'ret': ret}

    def week(self):
        today = datetime.datetime.now().date()
        weekday = datetime.datetime.now().date() - datetime.timedelta(weeks=1)
        customer_list = Customer.objects.filter(deal_date__gt=weekday, deal_date__lt=today)
        ret = getattr(self, 'get_userinfo_data')(weekday, today)
        return {'customer_list': customer_list, 'ret': ret}

    def month(self):
        today = datetime.datetime.now().date()
        month = datetime.datetime.now().date() - datetime.timedelta(weeks=4)
        customer_list = Customer.objects.filter(deal_date__gt=month, deal_date__lt=today)
        ret = getattr(self, 'get_userinfo_data')(month, today)
        return {'customer_list': customer_list, 'ret': ret}


class ClassStudents(View):
    def get(self, request, class_id):
        class_obj = ClassList.objects.get(pk=class_id)
        student_list = Student.objects.filter(class_list=class_id)
        next = '/?next=%s'% request.path
        return render(request, 'classstudent.html', {'student_list': student_list, 'class_obj': class_obj, 'next': next})
    def post(self, request, class_id):
        pass


class Students(View):
    def get(self, request):
        student_list = Student.objects.filter(class_list__isnull=True)
        class_list = ClassList.objects.all()
        return render(request, 'student_list.html', {'student_list': student_list, 'class_list': class_list})
    def post(self, request):
        action = request.POST.get('action')
        pk_list = request.POST.getlist('pk_list')
        for pk in pk_list:
            student_obj = Student.objects.filter(id=pk).first()
            student_obj.class_list.set(action)
        return redirect('/student/list/')



class AddStudent(View):
    def get(self, request):
        form = StudentModelForm(request)
        return render(request, 'add_student.html', {'form': form})

    def post(self, request):
        form = StudentModelForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/list/')
        else:
            return render(request, 'add_student.html', {'form': form})


class EditStudent(View):
    def get(self, request, id):
        student_obj = Student.objects.filter(pk=id).first()
        form = StudentModelForm(request, instance=student_obj)
        return render(request, 'editstudent.html', {'form': form})

    def post(self, request, id):
        student_obj = Student.objects.get(pk=id)
        form = StudentModelForm(request, request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('/student/list/')
        else:
            return render(request, 'editstudent.html', {'form': form})


class DeleStudent(View):
    def get(self, request, id):
        Student.objects.filter(pk=id).delete()
        return redirect('/student/list/')

class DeleClassStudent(View):
    def get(self, request, id):
        next = request.GET.get('next')
        student = Student.objects.filter(pk=id)
        student_id = student.values('class_list')[0]['class_list']
        student.first().class_list.remove(student_id)
        return redirect(next)





def loginout(request):
    auth.logout(request)
    return redirect('/login/')




class PersonalData(View):
    def get(self, request):
        user_data = UserInfo.objects.get(pk=request.session['user_id'])
        form = PersonalDataModelForm(request, instance=user_data)
        return render(request, 'personal_home.html', {'form': form, 'user_data': user_data})
    def post(self, request):
        user_data = UserInfo.objects.get(pk=request.session['user_id'])
        form = PersonalDataModelForm(request, request.POST, instance=user_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return render(request, 'personal_home.html', {'form': form})


class Permissions(View):
    def get(self, request):
        val = request.GET.get('q')
        opt = request.GET.get('opt')
        opt = str(opt) + '__contains'
        current_page = request.GET.get('page', '1')
        base_url = 'http://localhost:8000/permission/list'
        permission_list = Permission.objects.all()
        if val:
            q = Q()
            q.children.append((opt, val))
            permission_list = permission_list.filter(q)
        pagination = Pagination(current_page, permission_list.count(), request, base_url, 10)
        permission_list = permission_list[pagination.start: pagination.end]
        next = '/?next=%s' % request.path
        return render(request, 'permission_list.html', {'permission_list': permission_list, 'next': next, 'pagination': pagination})


class AddPermission(View):
    def get(self, request):
        form = PermissionModelForm(request)
        return render(request, 'add_permission.html', {'form': form})

    def post(self, request):
        form = PermissionModelForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/permission/list/')
        else:
            return render(request, 'add_permission.html', {'form': form})

class EditPermission(View):
    def get(self, request, permission_id):
        permission_obj = Permission.objects.get(pk=permission_id)
        form = PermissionModelForm(request, instance=permission_obj)
        return render(request, 'updatepermission.html', {'form': form})

    def post(self, request, permission_id):
        next = request.GET.get('next')
        permission_obj = Permission.objects.get(pk=permission_id)
        form = PermissionModelForm(request, request.POST, instance=permission_obj)
        if form.is_valid():
            form.save()
            return redirect(next)
        else:
            return render(request, 'updatepermission.html', {'form': form})


class DelePermission(View):
    def get(self, request, permission_id):
        Permission.objects.filter(pk=permission_id).delete()
        return redirect('/permission/list/')


class AssignPermissions(View):
    def get(self, request):
        user_list = UserInfo.objects.all()
        next = '/?next=%s' % request.path
        return render(request, 'assignpermissions.html', {'user_list': user_list, 'next': next})


class EditRole(View):
    def get(self, request, role_id):
        role_obj = Role.objects.filter(pk=role_id).first()
        form = RoleModelForm(request, instance=role_obj)
        return render(request, 'editrole.html', {'form': form})

    def post(self, request, role_id):
        next = request.GET.get('next')
        role_obj = Role.objects.filter(pk=role_id).first()
        form = RoleModelForm(request, request.POST, instance=role_obj)
        if form.is_valid():
            form.save()
            return redirect(next)
        else:
            return render(request, 'editrole.html', {'form': form})

class RoleView(View):
    def get(self, request):
        role_list = Role.objects.all()
        next = '/?next=%s' % request.path
        return render(request, 'role_list.html', {'role_list': role_list, 'next': next})

    def post(self, request):
        pass

class AddRole(View):
    def get(self, request):
        form = RoleModelForm(request)
        return render(request, 'add_role.html', {'form': form})

    def post(self, request):
        form = RoleModelForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/role/list/')
        else:
            return render(request, 'add_role.html', {'form': form})

class DeleRole(View):
    def get(self, request, role_id):
        Role.objects.filter(pk=role_id).delete()
        return redirect('/role/list/')

class EditUser(View):
    def get(self, request, user_id):
        user_obj = UserInfo.objects.filter(pk=user_id).first()
        form = UserInfoModelForm(request, instance=user_obj)
        return render(request, 'edituser.html', {'form': form})

    def post(self, request, user_id):
        user_obj = UserInfo.objects.filter(pk=user_id).first()
        form = UserInfoModelForm(request, request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('/assign_permissions/')
        else:
            return render(request, 'edituser.html', {'form': form})


