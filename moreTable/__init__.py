from os import path
from django.apps import AppConfig
# 要修改名称的app，我的是common;
# app名称不能有大小写区别
# default_app_config = 'moreTable.apps.Test'

VERBOSE_APP_NAME = '多表测试'


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME


default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'