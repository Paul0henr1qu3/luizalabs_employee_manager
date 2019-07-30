from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^employee/$', views.EmployeeList.as_view(), name='employee-list'),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name='employee-detail')

]