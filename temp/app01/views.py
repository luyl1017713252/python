from django.shortcuts import render

# Create your views here.

def index(request):
    '''
        模板语法 有render来进行渲染的
        1、渲染变量
            {{}}
            fitter 过滤器 | 过滤的名称
        2、渲染标签
            {% %}
            for 循环标签
            if 判断标签
    :param request:
    :return:
    '''
    name = 'Tomtu'
    age = 18
    books = ['金瓶梅', '红楼梦', '三国演义', '水浒传']
    info = {'name': 'Jerryliu', 'age': '28', 'gender': 'other'}
    class Animal(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def run(self):
            print('running')
    tomtu = Animal('tomtu', 18)
    jerry = Animal('jerryliu', 28)
    jack = Animal('jackzeng', 20)
    person_list = [tomtu, jerry, jack]
    from datetime import datetime
    now = datetime.now()
    file_size = 1234
    books_list = []
    shi = 'Falling in love with yourself first doesn’t make you vain or selfish, it makes you indestructible. '
    link = '<a href="https://www.baidu.com">点我</a>'
    tag = '<script>alert("123")</script>'
    age = 18
    # return render(request, 'index.html', {'name': name, 'age': age, 'books': books, 'info': info})
    return render(request, 'index.html', locals())

    # locals() 会将当前函数下的所有变量都形成字典发送给浏览器