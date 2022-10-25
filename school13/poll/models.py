from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_code=models.IntegerField(null=True,verbose_name="Employee Code")
    emp_name=models.CharField(max_length=20,verbose_name="Employee Name")
    emp_company=models.CharField(max_length=25,verbose_name="Employee Company Name")
    emp_address=models.TextField(default="xyz",verbose_name="Employee Address")
    emp_salary=models.IntegerField(null=True,verbose_name="Employee Current Salary")
    group=models.BooleanField(default=True)
    emp_email=models.EmailField(default="asd@gmail.com")
    webportal=models.URLField(default="www.google.com")
    # joining_date=models.DateField()


    # def __str__(self):
    #     return self.emp_name