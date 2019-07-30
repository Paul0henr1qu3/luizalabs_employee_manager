from django.contrib import admin
from .models import Employee

class EmployeeModelAdmin(admin.ModelAdmin):
    # Name of columns that will be displayed in admin mode
    list_display = ('pk', 'name', 'email', 'department')

admin.site.register(Employee, EmployeeModelAdmin)
