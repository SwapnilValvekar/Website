from django.shortcuts import render
from django.http import HttpResponse


def courses(request):
    return HttpResponse('<h1>Hello Welcome to PFSD </h1>')


def raj(request, course_id):
    return HttpResponse('<h1>Swapnil</h1>')


def hello(request):
    return render(request, 'hello.html')


def index(request):
    return render(request, 'index.html')
