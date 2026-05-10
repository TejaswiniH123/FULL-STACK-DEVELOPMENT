from django.shortcuts import render, redirect
from .models import Student, Course


def home1(request):
    return render(request, 'homepage.html')


def studentlist(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'student_list': students})


def courselist(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'course_list': courses})


def register(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')

        selected_student = Student.objects.get(id=student_id)
        selected_course = Course.objects.get(id=course_id)

        selected_student.enrollment.add(selected_course)

        return redirect('/enrolledlist/')

    return render(request, 'register.html', {
        'student_list': Student.objects.all(),
        'course_list': Course.objects.all()
    })


def enrolledStudents(request):
    courses = Course.objects.all()
    student_list = None
    selected_course = None

    if request.method == "POST":
        course_id = request.POST.get('course')
        selected_course = Course.objects.get(id=course_id)
        student_list = selected_course.students.all()

    return render(request, 'enrolledlist.html', {
        'Course_List': courses,
        'student_list': student_list,
        'course': selected_course
    })