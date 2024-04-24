from django.db import models


class Book(models.Model):
    name = models.CharField('Наименование', max_length=20)
    title = models.CharField('Заголовок', null=True, max_length=30)
    author = models.CharField('Автор', max_length=30)
    description = models.CharField('Описание', null=True, max_length=512)
    price = models.IntegerField('Цена', max_length=5)
