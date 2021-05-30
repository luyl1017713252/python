from django.contrib import admin

# Register your models here.
from app01.models import User, Role, Permission

admin.site.register(User)
admin.site.register(Role)
class PermissionConfig(admin.ModelAdmin):
    list_display = ['pk', 'title', 'url']
    ordering = ['pk']
admin.site.register(Permission,PermissionConfig)