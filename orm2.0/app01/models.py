from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE, null=True)  # 级联删除
    authors = models.ManyToManyField(to='Author')


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    email = models.CharField(max_length=32)
    ad = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    addr = models.CharField(max_length=32)
    tel = models.IntegerField()

# 创建多对多关联关系表
# class Book2Author(models.Model):
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
#     author = models.ForeignKey(to='Author', on_delete=models.CASCADE)