# 自定义中间件
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


# class PrintIPMiddleWare(MiddlewareMixin):
#     def process_request(self, request):
#         print(request.META.get('REMOTE_ADDR'))

class M1(MiddlewareMixin):
    def process_request(self, request):
        print('m1 process_request')
        return HttpResponse('M1 return data')

    def process_response(self, request, response):
        print('m1 process_response')
        return HttpResponse('M1 return process_response')
    def process_view(self, request, callback):
        pass


class M2(MiddlewareMixin):
    def process_request(self, request):
        print('m2 process_request')