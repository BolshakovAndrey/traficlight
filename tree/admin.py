from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(DjangoMpttAdmin):
    list_display = ('pk', 'structure', 'full_name', 'position', 'emp_date', 'salary', 'parent')
