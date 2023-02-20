
from django.contrib import admin
from django.urls import path
from poll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.home,name='home'),
    # path("home/",views.home,name='home'),
    # path("/home/",views.home,name='home'),
    # path("home//",views.home,name='home'),
    # path("home/<my_name>",views.home,name='home'),
    # # int 
    # path("home/<int:my_id>",views.home,name='home'),
    # path("home/<int:my_id>/<int:my_id1>",views.home,name='home'),
    # slug
    path("home/<slug:name>",views.home,name='home'),


]