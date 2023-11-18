from django.contrib import admin

# Register your models here.
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'department_id', 'department', 'matric_number', 
        'state_of_origin', 'date_of_birth'
        )
    search_fields = ('name', 'matric_number', 'department_id')

