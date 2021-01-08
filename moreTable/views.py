from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from moreTable import models
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

def add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))
    return HttpResponse(book)
def add_book_author(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)
    return HttpResponse(book)
def add_b2a(request):
    # 添加多对多关联关系
    book_obj = models.Book.objects.get(id=2)
    # author_list = models.Author.objects.filter(id__gt=1)
    # book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
    # 方式二：传对象 id
    book_obj.authors.add(*[1, 4])  # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中
    return HttpResponse("ok")
def search1(request):
    # 查找出书籍关联出版商的城市
    book = models.Book.objects.filter(pk=1).first()
    res = book.publish.city
    print(res, type(res))
    return HttpResponse(res)
def search2(request):
    # 反向查找出出版商所出的书籍
    pub = models.Publish.objects.filter(name="华山出版社").first()
    res = pub.book_set.all()
    mes = ''
    for i in res:
        mes += '《'+i.title+'》'
    return HttpResponse(mes)
def search3(request):
    # res = models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
    # print(res)
    res = models.Book.objects.annotate(c=Count("authors__name")).values("title", "c")
    print(res)
    return HttpResponse(res)