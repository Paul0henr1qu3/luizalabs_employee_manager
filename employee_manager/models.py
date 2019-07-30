from django.db import models

# Create your models here.
class Employee(models.Model):
    '''
        Model that will store employee information
    '''
    class Meta:

        db_table = 'employee'

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.title

