from msilib.schema import Class
from django.contrib import admin

# Register your models here.


from .models import Customer, Employee


# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_code',
                    'emp_name', 'emp_company',
                    'emp_address', 'emp_salary',
                    'group', 'emp_email',
                    'webportal', 'joining_date')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('emp_code', 'emp_name', 'emp_company', 'emp_address',
                    'emp_salary', 'group', 'joining_date', 'joining_date_time',)
