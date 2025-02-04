from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import StudentForm


def student_list(request):
    students=Student.objects.all()
    return render(request, 'student_list.html', {'students':students})

def student_detail(request,id):
    student=get_object_or_404(Student,id=id)
    return render(request, 'student_detail.html', {'student': student})

def student_create(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm()
    return render(request,'student_form.html',{'form':form})

def student_update(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=="POST":
        form = StudentForm(request.POST,instance=student)
        if  form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm(instance=student)
    return render(request,'student_form.html',{'form':form})

def student_delete(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request,'student_delete.html',{'student':student})


