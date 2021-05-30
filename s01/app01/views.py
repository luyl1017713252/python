from django.shortcuts import render , HttpResponse
from urllib.parse import parse_qs
from datetime import datetime
# Create your views here.

def timer(request):
    time = datetime.now().strftime('%Y-%m-%d %x')
    return HttpResponse(time)

def login(request):
    return render(request, 'login.html')

def auth(request):
    # 拿到用户名密码
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    import pymysql
    conn = pymysql.connect(user='root',
                           password="root",
                           host='localhost',
                           db='web',
                           port=3306, )
    cur = conn.cursor()
    sql = 'select * from userinfo where user=%s and pwd=%s'
    res = cur.execute(sql, (user, pwd))
    # 返回结果
    if res:
        return HttpResponse('登录成功')
    else:
        return HttpResponse('登录失败')
    return HttpResponse('fail')

def special_case_2003(request):
    return HttpResponse('2003')

def special_case_year(request, year):
    return HttpResponse(year)
def special_case_year_month(request, year, month):
    return HttpResponse(year, month)