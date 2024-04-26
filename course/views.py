from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher
# Create your views here.


def home_view(request):
    courses = Course.objects.all().order_by('-id')[:3]
    teachers = Teacher.objects.all().order_by('-id')[:3]
    context = {'courses': courses, 'teachers': teachers}
    return render(request, 'index.html', context)


def courselist_view(request):
    courses = Course.objects.all()
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    print(search)
    if search:
        courses = courses.filter(name__icontains=search)
    if tag:
        courses = courses.filter(tag__contains=tag)
    context = {'courses': courses, 'tag': tag, 'search': search}
    return render(request, 'kurslar.html', context)


def course_detail_view(request, pk):
    course = get_object_or_404(Course, id=pk)
    context = {'course': course}
    return render(request, 'course_detail.html', context)


def teachers_list_view(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)


def teachers_detail_view(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    context = {'teacher': teacher}
    return render(request, 'teacher_detail.html', context)
