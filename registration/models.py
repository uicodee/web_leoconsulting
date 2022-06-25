from django.db import models


class User(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)
    user_id = models.BigIntegerField(verbose_name='ID пользователя', null=False)
    name = models.CharField(max_length=50, verbose_name='Никнейм')
    username = models.CharField(max_length=150, verbose_name='Юзернейм', null=True)
    language = models.CharField(max_length=5, verbose_name='Язык')

    def __str__(self):
        return self.name


class Application(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.CharField(max_length=150, verbose_name='Email')
    region = models.CharField(max_length=75, verbose_name='Регион')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    status = models.CharField(max_length=100, null=False, default='new')


class Region(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)
    region_name = models.CharField(max_length=75, verbose_name='Регион', null=False)

    def __str__(self):
        return self.region_name
