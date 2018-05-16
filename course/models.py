import datetime
from django.db import models
from information.models import UserInfor


# Create your models here.
class CourseClassFirst(models.Model):
    name = models.CharField(choices=(('it', u"IT互联网"), ('language', u'语言留学'), ('design', u'创意设计'), ('life', u'兴趣生活'),
                                     ('plant', u'生产种植'), ('edu', u'升学考研'), ('certificate', u'公培考证')),
                            max_length=15, verbose_name=u'第一分类')

    class Meta:
        verbose_name = u"第一分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseClassSecond(models.Model):
    sort2 = models.ForeignKey(CourseClassFirst, verbose_name='第一分类')
    name = models.CharField(verbose_name='第二分类', max_length=30)

    class Meta:
        verbose_name = '第二分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseClassThird(models.Model):
    sort3 = models.ForeignKey(CourseClassSecond, verbose_name='第二分类')
    name = models.CharField(verbose_name='学科名称', max_length=30)

    class Meta:
        verbose_name = '第三类学科'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    sort4 = models.ForeignKey(CourseClassThird, verbose_name='第三分类')
    name = models.CharField(verbose_name='课程名称', max_length=30)
    price = models.IntegerField(verbose_name='课程价格')
    learn_time = models.CharField(verbose_name='课程时长', max_length=10)
    nums = models.IntegerField(verbose_name='购买人数', default=0)
    image = models.ImageField(verbose_name='课程封面', upload_to='course/%Y/%m')
    describe = models.ImageField(verbose_name='课程简介', max_length=100)
    click_num = models.IntegerField(verbose_name='点击人数', default=0)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    lesson_course = models.ForeignKey(Course, verbose_name='课程名')
    name = models.CharField(verbose_name='课程名', max_length=40)
    time = models.DateTimeField(default=datetime.datetime.now, verbose_name='课程时间')

    class Meta:
        verbose_name = '章节 '
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher_name = models.CharField(verbose_name='老师名字', max_length=20)
    teacher_course = models.ForeignKey(Course, verbose_name='课程名')
    teacher_des = models.CharField(verbose_name='老师描述', max_length=100)
    teacher_image = models.ImageField(verbose_name='头像', upload_to='teacher/%Y/%m', default='')

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name


class Buy(models.Model):
    user = models.ForeignKey(UserInfor, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='购买时间')

    class Meta:
        verbose_name = '买方'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
