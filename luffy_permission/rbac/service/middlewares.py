import re

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin



class PermissionsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.path)
        if request.path[len(request.path)-1] != '/':
            request.path = request.path + '/'
        for item in ['/login/', '/admin/*', '/reg/', '/valid_img/', '^/$', '/logout/', '/index/']:
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
            # if item == '^/updatecustomers/(\d+)/$':
            #     print(ret, request.path)
            if ret:
                request.show_id = item['pid'] or item['id']
                return None
        return HttpResponse('无权访问')