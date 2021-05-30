from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.urls import reverse

from app01.models import Book


def add(request):
    if request.method == 'POST':
        book = request.POST.dict()
        del book['csrfmiddlewaretoken']
        book = Book.objects.create(**book)
        # book = Book.objects.create(title='葵花宝典', price='2' ,pub_daye='2021-3-18', pub_lish='C190701出版社')
        return redirect(reverse('books'))
    else:
        return render(request, 'add_book.html')


def books(request):
    book_list = Book.objects.order_by('id').all()
    return render(request, 'books.html', {'book_list': book_list})


def delete(request, book_id):
    Book.objects.filter(id=book_id).delete()
    return redirect(reverse('books'))


def update(request, book_id):
    if request.method == 'POST':
        book = request.POST.dict()
        del book['csrfmiddlewaretoken']
        book['id'] = book_id
        Book.objects.filter(id=book_id).delete()
        Book.objects.create(**book)
        return redirect(reverse('books'))
    else:
        book_up_list = Book.objects.filter(id=book_id)
        return render(request, 'update_book.html', {'book_up_list': book_up_list})

def query(request):
    # 1.all() 方法 返回 queryset
    # book_list = Book.objects.all()
    # print(book_list)

    # 2.filter 方法 返回 queryset
    # book = Book.objects.filter(title='葵花宝典',price=10)
    # print(book)

    # 3.get方法 是一个model对象
    # book = Book.objects.get(title='java')
    # print(book.price)

    # 4.first() last() 返回对象 model
    # book = Book.objects.all()[0]
    # print(book.price)
    # book = Book.objects.all().first()
    # print(book.pub_date)
    # book = Book.objects.all().last()
    # print(book.pub_lish)

    # 5.exclude 返回的是queryset 包含了条件以外的所有不匹配对象
    # book = Book.objects.exclude(price=1000)
    # print(book)

    # 6.order_by
    # book = Book.objects.all().order_by('-price','-id')
    # print(book)

    # 7.count 计数  返回 整数
    # book = Book.objects.all().count()
    # print(book)

    # 8.reverse() 反转
    # book = Book.objects.all().order_by('price').reverse()
    # print(book)

    # 9.exists()
    # if Book.objects.exists():
    #     print('有数据')

    # 10.values 返回的也是queryset
    # book = Book.objects.all().values('title','price')
    # print(book)

    # 11.values_list
    # book = Book.objects.all().values_list()
    # print(book)

    # 模糊查询
    # book = Book.objects.filter(price__lte='10')
    # print(book)
    # book = Book.objects.filter(price__range=[1,10])
    # print(book)
    # book = Book.objects.filter(title__istartswith='py')
    # print(book)
    book = Book.objects.filter(pub_date__year=2020, pub_date__month=3)
    print(book)
    return HttpResponse('ok')
