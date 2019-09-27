from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class Platform(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    name = models.CharField("Название платформы", max_length=100)
    address = models.CharField("Адрес", max_length=200)
    tel = models.CharField("Телефонный номер", max_length=20)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)


class Volunteer(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    fio = models.CharField("ФИО", max_length=150)
    name = models.CharField("Имя", max_length=60)
    surname = models.CharField("Фамилия", max_length=60)
    patronymic = models.CharField("Отчество", max_length=60)
    bio = models.TextField("Биография", max_length=1000)
    tel = models.CharField("Телефонный номер", max_length=20)
    email = models.EmailField("Email", max_length=50)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)

