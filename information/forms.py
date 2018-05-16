#!/usr/bin/python
# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
from .models import UserInfor


class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha_0 = CaptchaField(error_messages={"invalid": '验证码错误'})


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": '验证码错误'})


class ResetPasswordForm(forms.Form):
    code = forms.CharField(required=True)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


class ChangePasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    oldpassword = forms.CharField(required=True, min_length=6)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


class ChangeMyinforFrom(forms.ModelForm):
    class Meta:
        model = UserInfor
        fields = ['image', 'name', 'phone', 'gender', 'introduce', 'qq', 'birthday']


class UpdateForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": '验证码错误'})


class UpdateSureForm(forms.Form):
    email = forms.EmailField(required=True)
