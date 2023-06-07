from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

from cherry.models import *
from cherry.serializers import *
from rest_framework.response import Response
from rest_framework import status

@api_view()
def MyEmployeesData(request):
    EQS=Employee.objects.all()
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)























