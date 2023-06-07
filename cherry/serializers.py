from rest_framework import serializers

from cherry.models import *



class EmployeeMS(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'













