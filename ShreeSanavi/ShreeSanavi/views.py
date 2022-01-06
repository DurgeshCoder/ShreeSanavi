from django.shortcuts import render
from course.models import *


def home(request):
    courses = Course.objects.all().order_by('-added_date')
    return render(request, 'index.html', {
        'courses': courses
    })
