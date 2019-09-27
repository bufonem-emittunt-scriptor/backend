from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


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

class News(models.Model):
    id = models.AutoField("ID новости", primary_key=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    content = models.TextField("Содержание новости", max_length=3000)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)

class BlackList(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    voluenteer = models.ForeignKey('Volunteer', on_delete=models.CASCADE)
    block_reason = models.TextField("Причина блокировки", max_length=1000)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)

class Contacts(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    fio = models.CharField("ФИО", max_length=150)
    name = models.CharField("Имя", max_length=60)
    surname = models.CharField("Фамилия", max_length=60)
    patronymic = models.CharField("Отчество", max_length=60)
    position = models.CharField("Должность", max_length=60)
    tel = models.CharField("Телефон", max_length=50)
    email = models.EmailField("Email", max_length=50)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)

class Event(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    description = models.TextField("Описание события", max_length=3000)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)
    start_date = models.DateTimeField("Дата начала", auto_now=False)
    end_date = models.DateTimeField("Дата окончания", auto_now=False)

class EventSubscription(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    voluenteer = models.ForeignKey('Volunteer', on_delete=models.CASCADE)

class Marks(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    mark = models.IntegerField("Оценка")

class PlatformReviews(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    voluenteer = models.ForeignKey('Volunteer', on_delete=models.CASCADE)
    review = models.CharField("Отзыв", max_length=250)
    mark = models.ForeignKey('Marks', on_delete=models.CASCADE)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)


class VolunteerReviews(models.Model):
    id = models.AutoField("Идентификатор", primary_key=True)
    voluenteer = models.ForeignKey('Volunteer', on_delete=models.CASCADE)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    review = models.CharField("Отзыв", max_length=250)
    mark = models.ForeignKey('Marks', on_delete=models.CASCADE)
    creation_date = models.DateTimeField("Дата создания", auto_now=True)
