from django.contrib import admin
from .models import CourseClassFirst, CourseClassSecond, CourseClassThird, Teacher, Course, Lesson


class FirstInline(admin.StackedInline):
    model = CourseClassFirst
    extra = 2


class SecondInline(admin.StackedInline):
    model = CourseClassSecond
    extra = 2


class ThirdInline(admin.StackedInline):
    model = CourseClassThird
    extra = 2


class CourseInline(admin.StackedInline):
    model = Course
    extra = 2


class TeacherInline(admin.StackedInline):
    model = Teacher
    extra = 2


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2


@admin.register(CourseClassFirst)
class CourseFirstAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']
    inlines = [SecondInline]


@admin.register(CourseClassSecond)
class CourseSecondAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort2']
    list_filter = ['name', 'sort2']
    list_per_page = 10
    search_fields = ['name', 'sort2']
    inlines = [ThirdInline]


@admin.register(CourseClassThird)
class CourseThirdAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort3']
    list_filter = ['name', 'sort3']
    list_per_page = 10
    search_fields = ['name', 'sort3']
    inlines = [CourseInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'learn_time', 'nums', 'image', 'describe', 'click_num', 'sort4']
    list_filter = ['name', 'price', 'learn_time', 'nums', 'image', 'describe', 'click_num', 'sort4']
    list_per_page = 10
    list_editable = ['price', 'learn_time', 'nums', 'image', 'describe', 'click_num']
    search_fields = ['name', 'price', 'learn_time', 'nums', 'image', 'describe', 'click_num', 'sort4']
    inlines = [TeacherInline, LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'time']
    list_filter = ['name', 'time', 'lesson_course']
    list_per_page = 10
    list_editable = ['time']
    search_fields = ['name', 'time', 'lesson_course']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'teacher_image', 'teacher_des']
    list_filter = ['teacher_name', 'teacher_image', 'teacher_des', 'teacher_course']
    list_per_page = 10
    list_editable = ['teacher_image', 'teacher_des']
    search_fields = ['teacher_name', 'teacher_image', 'teacher_des', 'teacher_course']



admin.site.site_header = '潭州课堂后台管理'
admin.site.site_title = '潭州课堂'
