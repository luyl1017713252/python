from django.contrib import admin

# Register your models here.
from app01.models import *

admin.site.register(UserInfo)
admin.site.register(Customer)
admin.site.register(Campuses)
admin.site.register(ClassList)
admin.site.register(Enrollment)
admin.site.register(PaymentRecord)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Student)
admin.site.register(ClassStudyRecord)
admin.site.register(StudentStudyRecord)