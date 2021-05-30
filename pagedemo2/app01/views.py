from django.shortcuts import render

# Create your views here.
from app01.models import Book
from django.core.paginator import Paginator

from app01.page import Pagination


def index(request):
    # book_list = []
    # for i in range(1, 101):
    #     book = Book(title='你的第一次%s' % i, price=100 + i)
    #     book_list.append(book)
    # Book.objects.bulk_create(book_list)
    # book_list = Book.objects.all()
    # pag = Paginator(book_list, 8)
    # print(pag.count)
    # print(pag.num_pages)  # 分页数 13
    # print(pag.page_range)  # range(1, 14)
    # print(pag.page(2))
    # page_num = request.GET.get('page', '2')
    # page_list = pag.page(page_num)
    # for p in page_num:
    #     print(p)
    # print(page_list.has_next())  # 是否有上一页
    # print(page_list.has_previous())  # 是否有下一页
    # print(page_list.next_page_number())  # 下一页数
    # print(page_list.previous_page_number())  # 上一页数
    current_page = request.GET.get('page', '1')
    book_list = Book.objects.all()
    base_url = 'http://localhost:8000/index/'
    pagination = Pagination(current_page, book_list.count(), request, base_url, 5)
    book_list = book_list[pagination.start: pagination.end]
    return render(request, 'index.html', {'book_list': book_list, 'pagination': pagination})
