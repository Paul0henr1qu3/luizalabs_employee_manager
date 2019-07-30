from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class EmployeeList(generics.ListCreateAPIView):
    '''
        View that implements the GET (List) methods 
        and the POST (Create) method.
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
        View that implements the GET, PUT, PATCH, 
        and DELETE methods.
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )