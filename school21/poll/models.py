from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    city=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=3,)
    emp_code=models.CharField(max_length=10)
    joining_date=models.DateTimeField(auto_now_add=False, auto_now=False)
    address=models.TextField()

    # objects=models.manager()
    student=models.manager()