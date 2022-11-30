from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Code(models.Model):
    # ...
    pass
class Users(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20, null=True)
    roll_number=models.CharField(max_length=20, null=True)
    code=models.ForeignKey(Code, on_delete=models.CASCADE, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

    def passcode(self):
        return "code"  + "roll_number"
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    
class Grade(models.Model):
    CATEGORY_CHOICES=(
        ('Grade1','Grade1'),
         ('Grade2','Grade2'),
          ('Grade3','Grade3'),
           ('Grade4','Grade4'),
            ('Grade5','Grade5'),
             ('Grade6','Grade6'),
              ('Grade7','Grade7'),
               ('Grade8','Grade8'),
        
    )
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
