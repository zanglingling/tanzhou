#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from information import views



urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register'),  # 注册
    url(r'^login/$', views.Login.as_view(), name='login'),  # 登录
    url(r'^logout/$', views.Logout.as_view(), name='logout'),  # 注销
    url(r'^index/$', views.Index.as_view(), name='index'),  # 首页
    url(r'^active/(.*?)/$', views.ActiveEmail.as_view(), name='active'),  # 激活用户
    url(r'^forgetpassword/$', views.ForgetPassword.as_view(), name='forgetpassword'),  # 忘记密码

    url(r'^reset/$', views.ReSetpassword.as_view(), name='reset'),  # 重置密码
    url(r'^changepassword/$', views.ChangePwView.as_view(), name='changepassword'),  # 修改密码


    url(r'^myinfo/$', views.MyInfor.as_view(), name='myinfo'),  # 个人信息
    url(r'^myhomework/$', views.MyHomework.as_view(), name='myhomework'),  # 个人作业
    url(r'^myorder/$', views.MyOrder.as_view(), name='myorder'),  # 个人订单
    url(r'^uadate_sub/$', views.UpdateSub.as_view(), name='uadate_sub'),  # 进入升级用户界面
    url(r'^update/$', views.UpdateSure.as_view(), name='update'),  # 确认信息



]
