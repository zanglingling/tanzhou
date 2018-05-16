#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courselist/$', views.CourseList.as_view(), name='courselist'),
    url(r'^details/(?P<course_id>.*)/$', views.CourseDetails.as_view(), name='details'),
    url(r'^lesson/(?P<course_id>.*)/$', views.CourseLesson.as_view(), name='lesson'),

]
