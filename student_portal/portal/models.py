from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class School_Admin(models.Model):
    """"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=30, unique=True)
    # other field


class Student(models.Model):
    """"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_admin = models.ForeignKey(School_Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    department_id = models.IntegerField(unique=True)
    matric_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=40)
    # other field

