from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    '''
        Class that will serialize and deserialize data in 
        json, xml, etc. representations.
    '''
    class Meta:

        model = Employee
        fields = ('name', 'email', 'department')

        