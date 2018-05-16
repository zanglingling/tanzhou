from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout, load_backend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .forms import UserRegisterForm, UserLoginForm, ForgetPasswordForm, ResetPasswordForm, ChangePasswordForm, \
    ChangeMyinforFrom, UpdateForm,UpdateSureForm
from .models import UserInfor, EmailVerify
from utils.send_email_email import sendEmail


# 注册用户
class Register(View):
    def get(self, request):
        register_form = UserRegisterForm()
        return render(request, 'user/register.html', locals())

    def post(self, request):
        register_form = UserRegisterForm(request.POST)  # 提交表单信息
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            email1 = UserInfor.objects.filter(email=email)
            if email1:
                return render(request, 'user/register.html', {'register_form': register_form,
                                                              'msg': '用户已存在'})
            else:
                password = register_form.cleaned_data['password']
                user = UserInfor()
                user.name = email
                user.email = email
                user.is_active = False
                user.password = make_password(password)
                user.save()
                sendEmail(email, 1)
                return render(request, 'user/login.html', {'message': '邮件已在路上，注意激活'})
        else:
            return render(request, 'user/register.html', locals())


# 自定义用户验证
class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfor.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception:
            return None


# 首页
class Index(View):
    def get(self, request):
        return render(request, 'index.htm')


# 登录用户
class Login(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        user_login = UserLoginForm(request.POST)
        if user_login.is_valid():
            user = authenticate(**user_login.cleaned_data)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('user:index'))
                else:
                    return render(request, 'user/login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'user/login.html', {'msg': '用户不存在或密码错误'})
        else:
            return render(request, 'user/login.html', {'user_login': user_login})


# 激活邮箱
class ActiveEmail(View):
    def get(self, request, num):
        record = EmailVerify.objects.filter(code=num).first()
        if record:
            email = record.email
            user = UserInfor.objects.filter(email=email).first()
            user.is_active = True
            user.save()
            return render(request, 'user/active_success.html')
        else:
            return render(request, 'user/login.html')


# 注销
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('user:index'))


# 忘记密码
class ForgetPassword(View):
    def get(self, request):
        forget_form = ForgetPasswordForm()
        return render(request, 'user/forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetPasswordForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data['email']
            user = UserInfor.objects.filter(email=email).exists()
            if user:
                sendEmail(email, 2)
                return render(request, 'user/send_success.html')
            else:
                return render(request, 'user/forgetpwd.html', {"msg": '用户不存在', 'forget_form': forget_form})
        else:
            return render(request, 'user/forgetpwd.html', locals())


# 重置密码
class ReSetpassword(View):
    def get(self, request):
        code = request.GET.get('code')
        return render(request, 'user/password_reset.html', locals())

    def post(self, request):
        reset_form = ResetPasswordForm(request.POST)

        if reset_form.is_valid():
            code = reset_form.cleaned_data['code']
            password1 = reset_form.cleaned_data['password1']
            password2 = reset_form.cleaned_data['password2']
            if EmailVerify.objects.filter(code=code).exists():
                if password1 != password2:
                    return render(request, 'user/password_reset.html', {'msg': '两次密码输入不一样'})
                else:
                    email1 = EmailVerify.objects.filter(code=code).first()
                    email = email1.email
                    user = UserInfor.objects.filter(email=email).first()
                    user.password = make_password(password2)
                    user.save()
                    return render(request, 'user/reset_success.html')
            else:
                return render(request, 'user/password_reset.html', {'msg': '激活链接有误'})
        else:
            return render(request, 'user/password_reset.html', locals())


# 个人信息
class MyInfor(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'my_info.html')

    def post(self, request):
        chang_myinfor_form = ChangeMyinforFrom(request.POST, request.FILES, instance=request.user)
        if chang_myinfor_form.is_valid():
            print(chang_myinfor_form.cleaned_data)
            chang_myinfor_form.save()
            return redirect(reverse('user:myinfo'))
        else:
            return render(request, 'my_info.html', locals())


class MyHomework(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'my_homework.html')


class MyOrder(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'my_order.html')


# 修改密码
class ChangePwView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'my_paasword.html', {'email': request.user.email})

    def post(self, request):
        changform = ChangePasswordForm(request.POST)
        email = request.user.email
        if changform.is_valid():
            oldpassword = changform.cleaned_data['oldpassword']
            user = authenticate(username=email, password=oldpassword)
            if user:
                password1 = changform.cleaned_data['password1']
                if password1 == changform.cleaned_data['password2']:
                    request.user.password = make_password(password1)
                    request.user.save()
                    return render(request, 'my_paasword.html', {'msg': '修改成功', 'email': email})
                else:
                    return render(request, 'my_paasword.html', {'msg': '两次密码不一致',
                                                                'email': email})
            else:
                return render(request, 'my_paasword.html', {'msg': '你输入的旧密码有误',
                                                            'email': email})
        else:
            return render(request, 'my_paasword.html', {'changform': changform})


class UpdateSub(View):
    def get(self, request):
        update_form = UpdateForm()
        return render(request, 'updata_sub.html', locals())

    def post(self, requset):
        update_form = UpdateForm(requset.POST)
        if update_form.is_valid():
            email = update_form.cleaned_data['email']
            user = UserInfor.objects.filter(email=email).first()
            if user:
                if user.is_active:
                    sendEmail(email, 3)
                    return render(requset, 'update_sucess.html')
                else:
                    return render(requset, 'updata_sub.html', {'msg': '用户未激活', 'update_form': update_form})
            else:
                return render(requset, 'updata_sub.html', {'msg': '用户不存在', 'update_form': update_form})
        else:
            return render(requset, 'updata_sub.html', {'update_form': update_form})


class UpdateSure(View):
    def get(self, request):
        code = request.GET.get('code')
        record = EmailVerify.objects.filter(code=code).first()
        email = record.email
        return render(request, 'update_sure.html',locals())
    def post(self,request):
        email_form = UpdateSureForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            user = UserInfor.objects.filter(email=email).first()
            if user:
                user.is_staff=True
                user.save()
                return redirect(reverse('user:index'))
            else:
                return render(request, 'update_sure.html', {'msg': '用户不存在'})
        else:
            return render(request, 'update_sure.html', locals())
