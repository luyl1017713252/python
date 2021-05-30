from django.db import models

# Create your models here.
class Foo(models.Model):
    title=models.CharField(max_length=32)