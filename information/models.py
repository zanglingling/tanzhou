import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户信息模型
class UserInfor(AbstractUser):
    name = models.CharField(verbose_name='昵称', max_length=40)
    image = models.ImageField(verbose_name='用户头像', upload_to='image/%Y/%m', default=None, null=True, blank=True)
    gender = models.SmallIntegerField(verbose_name='性别', choices=((1, '男'), (0, '女')), default=1)
    phone = models.CharField(verbose_name='手机', max_length=11, blank=True, null=True, )
    qq = models.CharField(verbose_name='QQ', max_length=12, blank=True, null=True)
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    introduce = models.CharField(verbose_name='简介', blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


# 轮播图模型
class Change(models.Model):
    changeName = models.CharField(verbose_name='轮播图名', max_length=30)
    changeImage = models.ImageField(upload_to='change/%Y/%m', max_length=100, default='')
    url = models.URLField(verbose_name='访问地址', max_length=100)
    createTime = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# 邮箱模型
class EmailVerify(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=20)
    email = models.EmailField(verbose_name='邮箱', max_length=25)
    choice = models.SmallIntegerField(verbose_name='选择', choices=((1, '注册'), (0, '找回密码')))
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱'
        verbose_name_plural = verbose_name
