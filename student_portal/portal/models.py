from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class School_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=30, unique=True)

class Department_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department_id = models.IntegerField(unique=True)
    # other fields...

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_admin = models.ForeignKey(School_Admin, on_delete=models.CASCADE, null=True, blank=True)
    department_admin = models.ForeignKey(Department_Admin, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    department_id = models.IntegerField(unique=True)
    student_department_id = models.IntegerField(unique=True, null=True, blank=True)
    matric_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=40)
    create_at = models.DateTimeField(default=datetime.now())
    # other fields...

    # other fields...

    # def save(self, *args, **kwargs):
    #     if self.department_admin:
    #         # Ensure department_admin can only access students with the same department_id
    #         self.department_admin_id = self.department_id
    #     super().save(*args, **kwargs)
