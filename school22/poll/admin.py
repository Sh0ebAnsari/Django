from django.contrib import admin

# Register your models here.
from .models import Student, Book ,Subject ,Post

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('id','book','Book_name','auther','price')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('id','name','no_of_ch','no_of_subject','student')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','content','sung_by')