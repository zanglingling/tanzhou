from django.shortcuts import render
from django.views import View
from .models import CourseClassThird, Course, CourseClassFirst, CourseClassSecond, Teacher, Lesson
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class CourseList(View):
    def get(self, request):
        first = CourseClassFirst.objects.all()
        second = CourseClassSecond.objects.all()
        third = CourseClassThird.objects.all()
        all_course = Course.objects.all()
        first_name = request.GET.get('first_name', '')
        hot_course = Course.objects.order_by('-click_num')[:4]
        if first_name:
            second = CourseClassSecond.objects.filter(sort2__name=first_name)
            all_course = Course.objects.filter(sort4__sort3__sort2__name=first_name)
        second_name = request.GET.get('second_name', '')
        if second_name:
            second = CourseClassSecond.objects.filter(name=second_name)
            third = CourseClassThird.objects.filter(sort3__name=second_name)
            all_course = Course.objects.filter(sort4__sort3__name=second_name)
        third_name = request.GET.get('third_name', '')
        if third_name:
            all_course = Course.objects.filter(sort4__name=third_name)
        price = request.GET.get('price', '')
        if price == '1':
            all_course = Course.objects.filter(price__gt=0)
        if price == '0':
            all_course = Course.objects.filter(price=0)
        key = request.GET.get('key', '')
        if key:
            all_course = Course.objects.filter(name__icontains=key)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 1, request=request)
        all_courses = p.page(int(page))
        return render(request, 'course_list.htm', {'all_courses': all_courses,
                                                   'first': first,
                                                   'second': second,
                                                   'third': third,
                                                   'price': price,
                                                   'first_name': first_name,
                                                   'second_name': second_name,
                                                   'third_name': third_name,
                                                   'hot_course': hot_course,
                                                   })


class CourseDetails(View):
    def get(self, request, course_id):

        course = Course.objects.filter(id=int(course_id)).first()
        course.click_num += 1
        course.save()
        teacher = Teacher.objects.filter(teacher_course_id=int(course_id)).first()
        if teacher:
            return render(request, 'course_detail.html', {'course': course, 'teacher': teacher})
        else:
            return render(request, 'course_detail.html', {'course': course})


class CourseLesson(View):
    def get(self, request, course_id):
        course = Course.objects.filter(id=int(course_id))
        teacher = Teacher.objects.filter(teacher_course_id=int(course_id)).first()
        lesson = Lesson.objects.filter(lesson_course_id=int(course_id))
        return render(request, 'course_lesson.html', locals())
