from django.urls import path
from Employee.views import *


urlpatterns = [
    path('employee/', EmployeeCreateView.as_view()),
    path('employee/<str:email>/', EmployeeDetailView.as_view())
]