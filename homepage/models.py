from time import time
from unicodedata import category
from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Course(models.Model):
    course_title=models.CharField(max_length=25 ,null=True)
    course=models.ImageField(null=True)
    date=models.DateTimeField(null=True)
    time=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Free','Free'),
        ('Paid','Paid'),
       
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)



class GradeOne(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)
class GradeTwo(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)
class GradeThree(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)
class GradeFour(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)
class GradeFive(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True, null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices = CATEGORY_CHOICES ,null=True)
class GradeSix(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    category=models.CharField(max_length=10,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)
class GradeSeven(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)

class GradeEight(models.Model):
    grade=models.CharField(max_length=25 ,null=True)
    title=models.CharField(max_length=25 ,null=True)
    subject=models.CharField(max_length=25 ,null=True)
    profile=models.FileField(null=True,upload_to='homepage/pdfs/')
    course_image=models.ImageField(null=True,upload_to='homepage/covers/')
    date=models.DateTimeField(auto_now=True,null=True)
    CATEGORY_CHOICES=(
        ('Paid','Paid'),
        ('Free','Free'),
        
    )
    category=models.CharField(max_length=6, choices =CATEGORY_CHOICES ,null=True)


