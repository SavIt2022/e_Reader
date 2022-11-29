from audioop import reverse
from http.client import HTTPResponse
import json
import logging
from django.shortcuts import render
from homepage.forms import *
from homepage.models import Course
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView





# Create your views here.
def xhome(request):
    return render (request,'xhome.html',{})
def grades(request):
    return render (request,'grades.html',{})
def subjects(request):
    return render (request,'subjects.html',{})

def payments(request):
    return render (request,'payments.html',{})

def add_course(request):
    if request.method=="POST":
        form=CourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CourseAdditionForm()
    return render(request,"add_course.html",{"form":form})

def courses_list(request):
    courses=Course.objects.all()
    return render(request,"courses_list.html",{ "courses":courses})

def edit_course(request,id):  
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=CourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=CourseAdditionForm(instance=course)
    return render(request,'edit_course.html',{"form":form})

def admin_dashboard(request):
    form=CourseAdditionForm()
    return render(request,"admin_dashboard.html",{
        "form":form,
    })
def school_admin_dashboard(request):
    form=CourseAdditionForm()
    return render(request,"school_admin_dashboard.html",{
        "form":form,
    })


def course(request,id):
    course=Course.objects.get(id=id)
    return render(request,'home.html',{'course':course})





# grade1
def add_grade1_course(request):
    if request.method=="POST":
        form=GradeOneCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeOneCourseAdditionForm()
    return render(request,"grades/first/add_grade1_course.html",{"form":form})

def grade1_course_list(request):
    courses=GradeOne.objects.all()
    return render(request,"grades/first/grade1_course_list.html",{ "courses":courses})


def edit_grade1_course(request,id):  
    course=GradeOne.objects.get(id=id)
    if request.method=="POST":
        form=GradeOneCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeOneCourseAdditionForm(instance=course)
    return render(request,'grades/first/edit_grade1_course.html',{"form":form})
from django.shortcuts import render

# grade2

def add_grade2_course(request):
    if request.method=="POST":
        form=GradeTwoCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeTwoCourseAdditionForm()
    return render(request,"grades/second/add_grade2_course.html",{"form":form})

def grade2_course_list(request):
    courses=GradeTwo.objects.all()
    return render(request,"grades/second/grade2_course_list.html",{ "courses":courses})


def edit_grade2_course(request,id):  
    course=GradeTwo.objects.get(id=id)
    if request.method=="POST":
        form=GradeTwoCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeTwoCourseAdditionForm(instance=course)
    return render(request,'grades/second/edit_grade2_course.html',{"form":form})

# grade3

def add_grade3_course(request):
    if request.method=="POST":
        form=GradeThreeCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeThreeCourseAdditionForm()
    return render(request,"grades/third/add_grade3_course.html",{"form":form})

def grade3_course_list(request):
    courses=GradeThree.objects.all()
    return render(request,"grades/third/grade3_course_list.html",{ "courses":courses})

def edit_grade3_course(request,id):  
    course=GradeThree.objects.get(id=id)
    if request.method=="POST":
        form=GradeThreeCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeThreeCourseAdditionForm(instance=course)
    return render(request,'grades/thrird/edit_grade3_course.html',{"form":form})

# grade4

def add_grade4_course(request):
    if request.method=="POST":
        form=GradeFourCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeFourCourseAdditionForm()
    return render(request,"grades/fourth/add_grade4_course.html",{"form":form})

def grade4_course_list(request):
    courses=GradeFour.objects.all()
    return render(request,"grades/fourth/grade4_course_list.html",{ "courses":courses})

def edit_grade4_course(request,id):  
    course=GradeFour.objects.get(id=id)
    if request.method=="POST":
        form=GradeFourCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeFourCourseAdditionForm(instance=course)
    return render(request,'grades/fourth/edit_grade4_course.html',{"form":form})

# grade5

def add_grade5_course(request):
    if request.method=="POST":
        form=GradeFiveCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeFiveCourseAdditionForm()
    return render(request,"grades/fifth/add_grade5_course.html",{"form":form})

def grade5_course_list(request):
    courses=GradeFive.objects.all()
    return render(request,"grades/fifth/grade5_course_list.html",{ "courses":courses})

def edit_grade5_course(request,id):  
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=GradeFiveCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeFiveCourseAdditionForm(instance=course)
    return render(request,'grades/fifth/edit_grade5_course.html',{"form":form})

# grade6

def add_grade6_course(request):
    if request.method=="POST":
        form=GradeSixCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeSixCourseAdditionForm()
    return render(request,"grades/sixth/add_grade6_course.html",{"form":form})

def grade6_course_list(request):
    courses=GradeSix.objects.all()
    return render(request,"grades/sixth/grade6_course_list.html",{ "courses":courses})

def edit_grade6_course(request,id):  
    course=GradeSix.objects.get(id=id)
    if request.method=="POST":
        form=GradeSixCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeSixCourseAdditionForm(instance=course)
    return render(request,'grades/sixth/edit_grade6_course.html',{"form":form})

    # grade7

def add_grade7_course(request):
    if request.method=="POST":
        form=GradeSevenCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeSevenCourseAdditionForm()
    return render(request,"grades/seventh/add_grade7_course.html",{"form":form})

def grade7_course_list(request):
    courses=GradeSeven.objects.all()
    return render(request,"grades/seventh/grade7_course_list.html",{ "courses":courses})

def edit_grade7_course(request,id):  
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=GradeSevenCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeSevenCourseAdditionForm(instance=course)
    return render(request,'grades/seventh/edit_grade7_course.html',{"form":form})

    # grade8

def add_grade8_course(request):
    if request.method=="POST":
        form=GradeEightCourseAdditionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=GradeEightCourseAdditionForm()
    return render(request,"grades/eighth/add_grade8_course.html",{"form":form})

def grade8_course_list(request):
    courses=GradeEight.objects.all()
    return render(request,"grades/eighth/grade8_course_list.html",{ "courses":courses})

def edit_grade8_course(request,id):  
    course=GradeEight.objects.get(id=id)
    if request.method=="POST":
        form=GradeEightCourseAdditionForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()       
    else:
        form=GradeEightCourseAdditionForm(instance=course)
    return render(request,'grades/eighth/edit_grade8_course.html',{"form":form})



from django_daraja.mpesa.core import MpesaClient

def index(request):
    cl = MpesaClient()
    phone_number = '0700111222'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HTTPResponse(response)