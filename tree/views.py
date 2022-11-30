from django.views.generic import ListView
from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
