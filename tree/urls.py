from django.contrib import admin
from django.urls import path
from tree.views import EmployeeListView

urlpatterns = [
    path('tree/', EmployeeListView.as_view(), name='employee-list'),
]