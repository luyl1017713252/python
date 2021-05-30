"""login4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    # path('enrollment/list/', views.EnrollmentView.as_view(), name='enrollment_list'),
    # path('add_enrollment/', views.AddUpdateEnrollment.as_view()),
    # re_path('updateenrollment/(\d+)', views.AddUpdateEnrollment.as_view(), name='updateenrollment'),
    # re_path('deleenrollment/(\d+)', views.DeleEnrollment.as_view()),
    # path('re_enrollment/', views.ReEnrollment.as_view()),
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('valid_img/', views.valid_img),
    path('reg/', views.reg),
    path('', views.index),
    path('customers/list/', views.Customers.as_view(), name='customers_list'),
    path('mycustomers/', views.Customers.as_view(), name='mycustomers'),
    re_path('delecustomers/(\d+)', views.DeleCustomers.as_view(), name='delecustomers'),
    path('loginout/', views.loginout),
    path('add_customer/', views.AddUpdateCustomersView.as_view(), name='add_customer'),
    re_path('updatecustomers/(\d+)', views.AddUpdateCustomersView.as_view(), name='updatecustomers'),
    path('consultRecord/list/', views.ConsultRecords.as_view(), name='consultrecord'),
    path('add_consultRecord/', views.AddConsultRecords.as_view()),
    re_path('del_con/(\d+)', views.DeleConsultRecords.as_view()),
    re_path('re_consultRecord/', views.ConsultRecords.as_view(), name='reconsultrecord'),

    path('paymentrecord/list/', views.PaymentRecordView.as_view(), name='paymentrecord_list'),
    path('add_paymentrecord/', views.AddPaymentRecord.as_view()),
    re_path('delepaymentrecord/(\d+)', views.DelePaymentRecord.as_view()),
    re_path('updatepaymentrecord/(\d+)', views.UpdatePaymentRecord.as_view(), name='updatepaymentrecord'),
    re_path('record_score/(\d+)', views.RecordScoreView.as_view(), name='record_score'),
    path('classstudyrecord/list/', views.ClassStudyRecords.as_view()),
    re_path('classstudyrecord/student/list/(\d+)', views.ClassStudents.as_view(), name='class_students'),
    re_path('add_classstudyrecord/', views.AddClassstudyRecord.as_view(), name='class_students'),
    path('student/list/', views.Students.as_view(), name='students'),
    path('student/add/', views.AddStudent.as_view(), name='addstudents'),
    re_path('student/edit/(\d+)', views.EditStudent.as_view(), name='editstudents'),
    re_path('student/dele/(\d+)', views.DeleStudent.as_view(), name='delestudents'),
    re_path('classstudents/dele/(\d+)', views.DeleClassStudent.as_view(), name='deleclassstudent'),


    path('personal/data/', views.PersonalData.as_view()),


    path('deal/list/', views.DealInfo.as_view()),


    path('search/', views.Search),


    path('permission/list/', views.Permissions.as_view(), name='permissions'),
    path('permission/add/', views.AddPermission.as_view(), name='add_permission'),
    re_path('updatepermission/(\d+)', views.EditPermission.as_view(), name='updatepermission'),
    re_path('delepermission/(\d+)', views.DelePermission.as_view(), name='delepermission'),
    path('assign_permissions/', views.AssignPermissions.as_view(), name='assign_permissions'),
    re_path('edit/roles/(\d+)', views.EditRole.as_view(), name='editrole'),
    path('role/list/', views.RoleView.as_view(), name='roles'),
    path('role/add/', views.AddRole.as_view(), name='addrole'),
    re_path('role/dele/(\d+)', views.DeleRole.as_view(), name='delerole'),
    re_path('user/edit/(\d+)', views.EditUser.as_view(), name='edituser')






]
