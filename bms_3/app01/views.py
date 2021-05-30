import json

from django.forms import widgets
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.urls import reverse

from app01 import models
from app01.models import Book, Publish, Author, AuthorDetail


def books(request):
    book_list = Book.objects.all()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, 'books.html',
                  {'book_list': book_list, 'publish_list': publish_list, 'author_list': author_list})


from django import forms


class BookForm(forms.Form):
    title = forms.CharField(label='书籍名称', max_length=32)
    price = forms.DecimalField(label='价格')
    pub_date = forms.DateField(label='出版日期', widget=widgets.TextInput(attrs={'type': 'data'}))


def add_book(request):
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        form = BookForm()
        return render(request, 'book_add.html',
                      {'publish_list': publish_list, 'author_list': author_list, 'form': form})
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        authors = request.POST.getlist('authors')
        book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish)
        book.authors.add(*authors)
        return redirect('/books/')


def del_book(request):
    book_id = request.POST.get('id_book')
    print(book_id)
    ret = Book.objects.filter(id=book_id).delete()
    if ret:
        return HttpResponse('True')
    else:
        return HttpResponse('False')


def up_book(request, book_id):
    if request.method == 'GET':
        book_up_list = Book.objects.filter(id=book_id)
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()

        book = Book.objects.filter(id=book_id).values('publish')[0]
        author = Book.objects.filter(id=book_id).values('authors')[0]
        publish_name = Publish.objects.filter(id=book['publish']).first()
        author_name = Author.objects.filter(id=author['authors']).first()
        return render(request, 'up_book.html',
                      {'book_up_list': book_up_list, 'publish_list': publish_list, 'author_list': author_list,
                       'publish_name': publish_name, 'author_name': author_name})
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        authors = request.POST.getlist('authors')
        # a_list = {'author_id': authors}
        print(authors)
        date_list = {'title': title, 'price': price, 'pub_date': pub_date, 'publish_id': publish}
        Book.objects.filter(id=book_id).update(**date_list)
        book = Book.objects.filter(id=book_id).first()
        book.authors.set(authors)
        return redirect(reverse('books'))


def publishs(request):
    publish_list = Publish.objects.all()
    return render(request, 'publishs.html', {'publish_list': publish_list})


def add_publish(request):
    if request.method == 'GET':
        return render(request, 'publish_add.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        Publish.objects.create(name=name, email=email)
        return redirect('/publishs/')


def del_publish(request, publish_id):
    Publish.objects.filter(id=publish_id).delete()
    return redirect('/publishs/')


def up_publish(request, publish_id):
    if request.method == 'GET':
        publish = Publish.objects.filter(id=publish_id)
        return render(request, 'up_publish.html', {'publish': publish})
    else:
        publish = request.POST.dict()
        del publish['csrfmiddlewaretoken']
        Publish.objects.filter(id=publish_id).update(**publish)
        return redirect('/publishs/')


def authors(request):
    author_list = Author.objects.all()
    return render(request, 'authors.html', {'author_list': author_list})


def add_author(request):
    if request.method == 'GET':
        return render(request, 'author_add.html')
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        tels = AuthorDetail.objects.create(tel=tel)
        author = Author.objects.create(name=name, age=age, email=email, ad=tels)
        return redirect('/authors/')


def del_author(request, author_id):
    author = Author.objects.filter(id=author_id)
    ad_id = author.values('ad_id')[0]['ad_id']
    author.delete()
    AuthorDetail.objects.filter(id=ad_id).delete()
    return redirect('/authors/')


def up_author(request, author_id):
    if request.method == 'GET':
        author = Author.objects.filter(id=author_id)
        return render(request, 'up_author.html', {'author': author})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        author = Author.objects.filter(id=author_id)
        author.update(name=name, age=age, email=email)
        AuthorDetail.objects.filter(id=author.values('ad_id')[0]['ad_id']).update(tel=tel)
        return redirect('/authors/')


def ajax_add_book(request):
    authors_list = []
    title = request.POST.get('title')
    price = str(format(int(request.POST.get('price')), '.2f'))
    pub_date = request.POST.get('pub_date')
    publish = request.POST.get('publish')
    authors = request.POST.getlist('authors')
    book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish)
    print(price)
    book.authors.add(*authors)
    count_book = Book.objects.all().count()
    publish_name = Publish.objects.filter(id=publish).first()
    authors_name = Author.objects.filter(id__in=authors)
    for i in authors_name:
        authors_list.append(i.name)
    data_dict = {
        'pd': 'true',
        'book_id': book.id,
        'count_book': count_book,
        'title': title,
        'price': price,
        'pub_date': pub_date,
        'publish_name': publish_name.name,
        'authors': authors_list
    }
    # print(authors, publish)
    if book:
        data_dict['pd'] = 'true'
    else:
        data_dict['pd'] = 'false'
    return HttpResponse(json.dumps(data_dict))
