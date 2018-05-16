#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
from django.core.mail import send_mail
from information.models import EmailVerify
from tanzhou.settings import EMAIL_FROM


def random_code():
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlNnMmOoPpQqRrSsTtUuVvWwXxYyZz012346789'
    length = len(chars)
    for i in range(16):
        str += chars[random.randint(0, length - 1)]
    return str


def sendEmail(email, num):
    emailrecord = EmailVerify()
    code = random_code()
    emailrecord.code = code
    emailrecord.email = email
    emailrecord.choice = num
    emailrecord.save()
    if num == 1:
        email_title = u"在线注册激活链接"
        email_body = u"请点击下面的链接激活你的账号：http://127.0.0.1:8000/user/active/{0}".format(code)
        email_stuate = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if num == 2:
        email_title = u"在线重置密码链接"
        email_body = u"请点击下面的链接激活你的账号：http://127.0.0.1:8000/user/reset/?code={0}".format(code)
        email_stuate = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if num == 3:
        email_title = u"在线升级用户链接"
        email_body = u"请点击下面的链接激活你的账号：http://127.0.0.1:8000/user/uadate_sure/?code={0}".format(code)
        email_stuate = send_mail(email_title, email_body, EMAIL_FROM, [email])
