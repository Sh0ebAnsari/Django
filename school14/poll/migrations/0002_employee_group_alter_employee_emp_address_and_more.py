# Generated by Django 4.1.2 on 2022-10-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='group',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_address',
            field=models.TextField(default='xyz', verbose_name='Employee Address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.IntegerField(null=True, verbose_name='Employee Code'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_company',
            field=models.CharField(max_length=25, verbose_name='Employee Company Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_name',
            field=models.CharField(max_length=20, verbose_name='Employee Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_salary',
            field=models.IntegerField(null=True, verbose_name='Employee Current Salary'),
        ),
    ]