from django.db import models

# Create your models here.


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()  # 2021-3-18 00:...
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE, null=False)  # 级联删除
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return f'title:{self.title}, publish:{self.publish}'


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return f'name:{self.name}, email:{self.email}'


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    email = models.CharField(max_length=32)
    ad = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'ad:{self.ad}, name:{self.name}'


class AuthorDetail(models.Model):
    addr = models.CharField(max_length=32)
    tel = models.BigIntegerField(max_length=20)

    def __str__(self):
        return f'tel:{self.tel}'

# 创建多对多关联关系表
# class Book2Author(models.Model):
#     book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
#     author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
