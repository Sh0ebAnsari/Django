from django.contrib import admin

# Register your models here.


from .models import Employee


# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','emp_code','emp_name','emp_company','emp_address','emp_salary','group','emp_email','webportal')