from django.contrib import admin

# Register your models here.
from .models import Student, School_Admin, Department_Admin


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = (
        'name', 'department_id', 'department', 'matric_number', 
        'state_of_origin', 'date_of_birth'
        )
    search_fields = ('name', 'matric_number', 'department_id')


@admin.register(School_Admin)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'department'
        )
    search_fields = ('user', 'name', 'department')

@admin.register(Department_Admin)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'department_id'
        )
    search_fields = ('user', 'name')
