from calendar import month
from lib2to3.fixes.fix_input import context

from django.shortcuts import render,get_object_or_404, redirect
from .models import Study
from .studyform import *




def stud(request):
    res= Study.objects.all()
    return render(request, 'study.html', {'res': res})


def test(request):
    # res= Study.objects.all()
    return render(request, 'index.html')

def studtest(request):

        context={
            'study_form':Study_form()
        }
        if request.method == "POST":

            study_form = Study_form(request.POST)

            if study_form.is_valid():
                study_form.save()

        return render(request,'studyform.html',context)




def allstudy(request):

    all_study= Study.objects.all()

    return render(request,'allstudy.html',{'all_study':all_study})


def studentUpdate(request,id):
    study = Study.objects.get(id=id)
    context ={
        'study_form' : Study_form(instance=study)
    }
    if request.method=='POST' :
        study_form = Study_form(request.POST, instance=study)

        if study_form.is_valid():
            study_form.save()
            return redirect('allstudy')
    return render(request, 'studyform.html', context)


def deletestudy(request,id):
    study = Study.objects.get(id=id)
    study.delete()
    return redirect('allstudy')

