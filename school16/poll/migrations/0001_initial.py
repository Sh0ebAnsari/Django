# Generated by Django 4.1.2 on 2022-10-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('weight', models.IntegerField()),
                ('brand', models.CharField(max_length=30)),
            ],
        ),
    ]