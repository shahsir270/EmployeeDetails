from django.shortcuts import render
from rest_framework.views import APIView
from Employee.serializers import *
from rest_framework.response import Response
from rest_framework import status
from Employee.models import *
from django.shortcuts import get_object_or_404

# Create your views here.
class EmployeeCreateView(APIView):
    serializer_class = EmployeeSerializer
    def get(self, request):
        serializer = self.serializer_class()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    serializer_class = EmployeeSerializer
    def get(self, request, email):
        employee = Employee.objects.filter(email=email).first()
        serializer = self.serializer_class(employee)
        if employee:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("employee is not exist", status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, email):
        employee = Employee.objects.filter(email=email).first()
        serializer = self.serializer_class(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, email):
        employee = Employee.objects.filter(email=email).first()
        if employee:
            employee.delete()
            return Response("employee is deleted", status=status.HTTP_200_OK)
        return Response("employee is not exist", status=status.HTTP_400_BAD_REQUEST)
        