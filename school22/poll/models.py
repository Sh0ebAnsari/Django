from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.name 


class Book(models.Model):
    book=models.OneToOneField(to=Student, on_delete=models.CASCADE , verbose_name="Owner")
    # book=models.OneToOneField(to=Student, on_delete=models.PROTECT , verbose_name="Owner")
    # book=models.OneToOneField(to=Student, on_delete=models.SET_NULL(), verbose_name="Owner")
    # book=models.OneToOneField(to=Student, on_delete=models.SET_DEFAULT() , verbose_name="Owner")
    # book=models.OneToOneField(to=Student, on_delete=models.SET(value="Hello") , verbose_name="Owner")
    # book=models.OneToOneField(to=Student, on_delete= models.DO_NOTHING() , verbose_name="Owner")

    Book_name=models.CharField(max_length=20)
    auther=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=6, decimal_places=2)


class Subject(models.Model):
    student=models.ForeignKey(to=Student, on_delete=models.CASCADE , verbose_name="Subject Chooser ")
    # student=models.ForeignKey(to=Student, on_delete=models.CASCADE , verbose_name="Subject Chooser",related_name="Book")
    name=models.CharField(max_length=10)
    no_of_ch=models.IntegerField()
    no_of_subject=models.IntegerField()


class Post(models.Model):
    user=models.ManyToManyField(User)
    title=models.CharField(max_length=10)
    content=models.TextField()


    def sung_by(self):
        return "".join([str(p)for p in self.user.all()])