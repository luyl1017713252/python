import re

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class PermissionsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path[len(request.path)-1] != '/':
            request.path = request.path + '/'
        for item in ['/login/', '/admin/*']:
            ret = re.search(item, request.path)
            if ret:
                return None
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')
        permissions_list = request.session['permissions_list']
        print(permissions_list)
        for item in permissions_list:
            item = '^%s$' % item
            ret = re.search(item, request.path)
            if ret:
                return None
        return HttpResponse('无权访问')