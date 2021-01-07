## 学习Django
---

### 新建app
---
* django-admin.py startapp app名称
* settings.py 中找到INSTALLED_APPS这一项，如下：
'''
  INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app名称',               
    )
'''
  
### 数据库
---
* 创建表结构
'python manage.py migrate'
* 让 Django 知道我们在我们的模型有一些变更
'python manage.py makemigrations app名称'
* 创建表结构
'python manage.py migrate app名称'
  
### 创建数据库超级管理员
---
* 创建超级用户
'python manage.py createsuperuser'