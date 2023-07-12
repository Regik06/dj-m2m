from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    student = Student.objects.order_by(ordering).prefetch_related('teachers')
    context = {'object_list': student}
    return render(request, template, context)


def add_teachers(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    for student in students:  # добавляем каждого учителя к каждому студенту.
        for teacher in teachers:
            student.teachers.add(teacher)

    return HttpResponse('Каждому ученику добавлены все учителя.')
