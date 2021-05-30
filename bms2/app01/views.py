from django.shortcuts import render, HttpResponse

# Create your views here.
from app01.models import Book, Publish, Author, Publish, AuthorDetail, Emp


def addrecord(request):
    # 添加记录  添加一本书   一对多 添加记录
    # Book.objects.create(
    #     title='python',
    #     price=188,
    #     pub_date='2021-3-23',
    #     publish_id=1,
    # )
    # publish = Publish.objects.filter(name='江软出版社').first()
    #
    # book = Book.objects.create(
    #     title='辟邪剑谱',
    #     price=1,
    #     pub_date='2021-3-20',
    #     publish=publish,
    # )
    # 多对多 添加记录 绑定关联关系
    # 方式1
    # tomtu = Author.objects.filter(name='tomtu').first()
    # jerry = Author.objects.filter(name='jerry').first()
    # book.authors.add(tomtu,jerry)
    # 方式2
    # book.authors.add(2)
    # 方式3
    # book.authors.add(*[1, 2])

    # 解除对象
    # tomtu = Author.objects.filter(name='tomtu').first()
    # book = Book.objects.filter(title='go').first()
    # # book.authors.remove(2)
    # book.authors.clear()

    # 解除再绑定
    # tomtu = Author.objects.filter(name='tomtu')
    # book = Book.objects.filter(id=1).first()
    # book.authors.set(tomtu)

    # 基于对象的跨表查询
    # 查询python这本书的出版社名字和邮箱
    # book = Book.objects.filter(title='python').first()
    # publish = Publish.objects.filter(pk=book.publish_id).first()
    # print(publish.name,publish.email)
    # book = Book.objects.filter(title='python').first()
    # print(book.publish)
    # print(book.publish.name, book.publish.email)

    # 查询江软出版社出版的所有书籍的名称
    # publish = Publish.objects.filter(name='江软出版社').first()
    # print(publish.book_set.all())
    # 一对多查询
    # 正向查询  关联属性所在的表的查询记录
    # 反向查询
    '''
                正向查询 book.publish.name
        Book  ---------------------------> Publish
            <----------------------------
                反向查询表名.关联属性表的名称(小写)_set.all()

    '''
    # 查询python这本书籍的作者的年龄
    # book = Book.objects.filter(title='python').first()
    # ret = book.authors.all().values('age')
    # print(ret)
    # 查询tomtu出版过的所有书籍的名称
    # tomtu = Author.objects.filter(name='tomtu').first()
    # print(tomtu.book_set.all())
    # 查询tomtu的手机号
    # tomtu = Author.objects.filter(name='tomtu').first()
    # print(tomtu.ad.tel)
    # 查询手机为888的作者名字
    ad = AuthorDetail.objects.filter(tel=888).first()
    print(ad.author.name)

    return HttpResponse('OK')


def query(request):
    # 基于双下划线的跨表查询  基于join来查询的 万能的双下划线
    # 正向查询是按字段  反向查询是按表名小写
    # 查询python这本书的出版社名字和邮箱
    # ret = Book.objects.filter(title='python').values('publish__name','publish__email')
    # print(ret)
    # ret = Publish.objects.filter(book__title='python').values('name','email')
    # print(ret)
    # 查询江软出版社出版的所有书籍的名称
    # ret = Book.objects.filter(publish__name='江软出版社').values('title')
    # print(ret)
    # ret = Publish.objects.filter(name='江软出版社').values('book__title')
    # print(ret)

    # 查询python这本书籍的作者的年龄
    # ret = Book.objects.filter(title='python').values('authors__age')
    # print(ret)
    # ret = Author.objects.filter(book__title='python').values('age')
    # print(ret)

    # 查询tomtu出版过的所有书籍的名称
    # ret = Book.objects.filter(authors__name='tomtu').values('title')
    # print(ret)
    # ret = Author.objects.filter(name='tomtu').values('book__title')
    # print(ret)

    # 查询手机号码为888的作者名字
    # ret = Author.objects.filter(ad__tel='888').values('name')
    # print(ret)
    # ret = AuthorDetail.objects.filter(tel='888').values('author__name')
    # print(ret)

    # 查询江软出版社出版的所有书籍名字以及作者的姓名
    # ret = Publish.objects.filter(name='江软出版社').values('book__title','book__authors__name')
    # print(ret)
    # ret = Book.objects.filter(publish__name='江软出版社').values('title','authors__name')
    # print(ret)
    # ret = Author.objects.filter(book__publish__name='江软出版社').values('name','book__title')
    # print(ret)
    # 手机号码为88开头的作者出版过的所有书籍名称以及出版社名称
    # ret = AuthorDetail.objects.filter(tel__startswith=88).values('author__book__title', 'author__book__publish__name')
    # print(ret)

    # ret = Author.objects.filter(ad__tel__startswith=88).values('book__title','book__publish__name')

    # 聚合函数  分组  sum avg min max count

    from django.db.models import Avg, Sum, Max, Min, Count
    # 查询所有书籍的平均价格
    # ret = Book.objects.all().aggregate(priceAvg=Avg('price'))

    # 查询所有书籍的个数
    # ret = Book.objects.all().aggregate(c=Count(1))

    # 查询所有书籍的最贵和最便宜的 所有书价格的和

    # 分组  单表分组
    # 查询书籍每一个出版社的id以及对应的书籍的个数
    # 如果对所有数据进行分组是没有意义的--单表
    # key：annotate前面的values的字段来进行group by
    # ret = Book.objects.values('publish_id').annotate(c=Count(1))

    # emp 员工表
    # id name age gender dep addr salary

    # 查询每一个部门的名称以及对应的员工的平均薪水
    # ret = Emp.objects.values('dep').annotate(Avg('salary'))

    # 查询每一个地区的名称以及员工的最大年龄
    # ret = Emp.objects.values('addr').annotate(Max('age'))

    # 单表查询按主键分组是没有意义的
    # ret = Emp.objects.values('id').annotate(Max('age'))

    # 跨表的分组查询
    # 查询每一个出版社的名称以及对应的书籍的平均价格
    # 方式1
    # ret = Publish.objects.values('id', 'name').annotate(Avg('book__price'))

    # 方式2
    # ret = Publish.objects.all().annotate(priceAvg=Avg('book__price'))

    # for publish in ret:
    #     print(publish.priceAvg)

    # 方式3
    # ret = Publish.objects.annotate(priceAvg=Avg('book__price'))
    # print(ret[0].priceAvg)
    # 查询每一个作者的名字以及书籍的最高价格
    # ret = Author.objects.values('name').annotate(Max('book__price'))

    # ret = Author.objects.annotate(bookMax=Max('book__price'))\
    #     .values('name', 'bookMax')

    # for author in ret:
    #     print(author.name, author.bookMax)
    # 查询每一个书籍的名称，以及对应的作者的个数
    # ret = Book.objects.values('title').annotate(c=Count('authors'))

    #
    # 查询作者数不止一个的书籍名称以及作者的个数 书的count(作者名字分组)大于1 显示书名+个数
    # ret = Book.objects.annotate(c=Count('authors')).filter(c__gt=1).values('title', 'c')
    # 根据一本图书作者的数量进行排序 升序
    # ret = Book.objects.annotate(c=Count('authors')).values('title', 'c').order_by('c')
    # 统计每一本以py开头的书籍的名称以及作者个数
    # ret = Book.objects.filter(title__startswith='py').annotate(c=Count('authors')).values('title', 'c')
    # print(ret)









    # F和Q函数
    # 查询评论数大于100的所有书籍的名称
    from django.db.models import F, Q
    ret = Book.objects.filter(comment_count__gt=100).values('title')
    # 查询评论数大于点赞数的书籍名称
    ret = Book.objects.filter(comment_count__gt=F('poll_count')).values('title')
    # 查询评论数大于2倍点赞数的书籍名称
    ret = Book.objects.filter(comment_count__gt=F('poll_count') * 2).values('title')
    # 给每一本书的价格增加100
    Book.objects.all().update(price=100+F('price'))
    # 查询价格大于300或者评论数大于3000的书籍
    Book.objects.filter(Q(price__gt=300 | Q(comment_count__gt=3000)))

    # 当我们要用字段做运算，用F函数
    # 当我们要使用或 和非运算 用Q函数 使用Q函数时 Q函数要放在前面

    print(ret)

    return HttpResponse('ok')
