# Generated by Django 4.1.2 on 2022-10-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_employee_group_alter_employee_emp_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_email',
            field=models.EmailField(default='asd@gmail.com', max_length=254),
        ),
    ]
