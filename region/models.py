from django.db import models
from django.conf import settings
# 引用AbstractUser更改user字段
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

# class NewUser(AbstractUser):
# 	new_field = models.CharField(max_length=100)

class Zone(models.Model):
    zoneName = models.CharField(max_length=32)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):              # __str__ on Python 3
        return self.zoneName
    # 用于给本表指定一个别名
    class Meta():
        verbose_name_plural = "区域"
class Department(models.Model):
    departmentName = models.CharField(max_length=32)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):              # __str__ on Python 3
        return self.departmentName
    # 用于给本表指定一个别名
    class Meta():
        verbose_name_plural = "部门"
class Place(models.Model):
    room = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    place = models.CharField(max_length=32)
    map = models.CharField(max_length=32)
    zoon = models.ForeignKey('Zone',on_delete=models.CASCADE)
    def __str__(self):
        res = self.room + self.area + self.place
        return res
    # 用于给本表指定一个别名
    class Meta():
        verbose_name_plural = "位置"