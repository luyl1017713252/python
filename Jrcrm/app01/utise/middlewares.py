import re

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AutuMiddleWares(MiddlewareMixin):
    def process_request(self, request):
        # 先拿到url路径
        path = request.path
        # 判断path是否是login或reg
        path_list = ['/login/', '/reg/', '/valid_img/', '/loginout/', '/personal/data/']
        if path in path_list:
            return None
        # 否则判断用户状态，重定向login
        if not request.user.is_authenticated:
            return redirect('/login/')


class PermissionsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path[len(request.path)-1] != '/':
            request.path = request.path + '/'
        for item in ['/login/', '/admin/*', '/reg/', '/valid_img/', '/loginout/', '/personal/data/', '/search/']:
            ret = re.search(item, request.path)
            if ret:
                return None
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')
        permissions_list = request.session['permissions_list']

        for item in permissions_list:
            path = '^%s$' % item['url']
            ret = re.search(path, request.path)
            if ret:
                # request.show_id = item['pid'] or item['id']
                return None
        return HttpResponse('无权访问')