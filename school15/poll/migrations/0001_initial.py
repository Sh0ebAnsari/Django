# Generated by Django 4.1.2 on 2022-10-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_code', models.IntegerField(null=True, verbose_name='Employee Code')),
                ('emp_name', models.CharField(max_length=20, verbose_name='Employee Name')),
                ('emp_company', models.CharField(max_length=25, verbose_name='Employee Company Name')),
                ('emp_address', models.TextField(default='xyz', verbose_name='Employee Address')),
                ('emp_salary', models.IntegerField(null=True, verbose_name='Employee Current Salary')),
                ('group', models.BooleanField(default=True)),
                ('emp_email', models.EmailField(default='asd@gmail.com', max_length=254)),
                ('webportal', models.URLField(default='www.google.com')),
                ('joining_date', models.DateField()),
            ],
        ),
    ]