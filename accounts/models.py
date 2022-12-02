from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_school_admin = models.BooleanField('Is school_admin', default=False)
    is_publisher = models.BooleanField('Is publisher', default=False)
    is_student = models.BooleanField('Is student', default=False)

    
