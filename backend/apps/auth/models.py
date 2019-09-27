from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class PlatformAuth(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField("Идентификатор", primary_key=True)
    # platform_id = models.ForeignKey()

