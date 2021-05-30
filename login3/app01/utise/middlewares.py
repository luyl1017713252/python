from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AutuMiddleWares(MiddlewareMixin):
    def process_request(self, request):
        # 先拿到url路径
        path = request.path
        # 判断path是否是login或reg
        path_list = ['/login/', '/reg/']
        if path in path_list:
            return None
        # 否则判断用户状态，重定向login
        if not request.user.is_authenticated:
            return redirect('/login/')