from django.contrib import admin


from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','author_name','title','desc','publish_date','user')