from django.shortcuts import render
from django.http import HttpResponse

from .models import  *

from .forms import *


def test2(request):
    # stud= Students.objects.all()
    stud = Students.objects.filter(name='hari').values()
    return render(request, 'student.html',{'stud':stud})


# Create your views here.
def home(request):
    # return HttpResponse('hello')
    return render(request,'home.html')
def index(request):
    # return HttpResponse('hello')
    return render(request,'index_old.html')

def test(request):
    # stud=Students.objects.all()
    stud = Students.objects.filter(name='hari').values()
    return render(request, 'student.html',{'stud':stud})

def test1(request):
    context={'students_form':Students_Form()}

    if request.method =="POST" :

        student_form= Students_Form(request.POST)
        print(request.POST)

        if student_form.is_valid():
            student_form.save()
    return render(request,'models.html', context)

def web(request):
    return render(request,'index.html')