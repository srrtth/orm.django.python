from django.urls import path

from . import views

urlpatterns = [
    path('employee/', views.create_employee),
    path('list_emp/', views.list_employees),
    path('del_emp/', views.del_emp_form)
]