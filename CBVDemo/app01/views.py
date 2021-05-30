from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def login(request):
    return render(request, 'login.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return HttpResponse('ok')