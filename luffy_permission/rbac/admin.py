from django.contrib import admin
from rbac import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'url']
    # 让列表里的字段可以在admin页面中直接修改添加
    list_editable = ['url']
    # 添加一个以title为搜索目标的搜索框
    search_fields = ['title']


admin.site.register(models.Permission, PermissionAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    # 不能直接用roles，roles是一个多对多的关系
    list_display = ['pk', 'name', 'get_role']

    # 创建一个用来查看每一个用户与其关联的全部角色
    def get_role(self, obj):
        return [role.title for role in obj.roles.all()]


admin.site.register(models.UserInfo, UserInfoAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'get_permissions']

    def get_permissions(self, obj):
        return [permission.title for permission in obj.permissions.all()]


admin.site.register(models.Role, RoleAdmin)


admin.site.register(models.Menu)





