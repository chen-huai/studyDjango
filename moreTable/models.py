from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")
    def __str__(self):              # __str__ on Python 3
        return self.title
    # 用于给本表指定一个别名
    class Meta():
        # verbose_name = "多表测试"
        verbose_name_plural = "书籍"

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()
    def __str__(self):              # __str__ on Python 3
        return self.name
    class Meta():
        verbose_name_plural = "出版社"

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)
    def __str__(self):              # __str__ on Python 3
        return self.name
    class Meta():
        verbose_name_plural = "作者"

class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()

    class Meta():
        verbose_name_plural = "作者详情"

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary =     models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)
class Dep(models.Model):
    title = models.CharField(max_length=32)