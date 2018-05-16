from django.contrib import admin
from .models import UserInfor, Change, EmailVerify


@admin.register(UserInfor)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone']
    list_filter = ['username', 'email', 'phone']
    list_per_page = 10
    list_editable = ['email', 'phone']
    search_fields = ['username', 'email', 'phone']
    fieldsets = (
        # 可以设置操作
        (u'账号信息', {
            'fields': ('username', 'name', 'email', 'gender','password')
        }),

        (u'权限', {
            'fields': ('groups', 'user_permissions')
        }),

        (u'状态', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),

        # 显示不是隐藏 classes, 样式是不是
        (u'其他信息', {
            'classes': ('collapse',),
            'fields': (
                'birthday', 'image', 'last_login', 'date_joined', 'introduce', 'first_name', 'last_name', 'qq',
                'phone'),
        }),
    )


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ['changeName', 'changeImage', 'url', 'createTime']
    list_filter = ['changeName', 'changeImage', 'url', 'createTime']
    list_per_page = 10
    list_editable = ['changeImage', 'url', 'createTime']
    search_fields = ['changeName', 'changeImage', 'url', 'createTime']
