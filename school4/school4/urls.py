"""school4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enroll import views as er
from poll import views as po

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enroll/course/',er.course,name='course-view'),
    path('enroll/fees/',er.enroll_fees,name='course-fees'),
    path('enroll/enroll_new_data/',er.enroll_data,name='enroll-new-data'),


    path('poll/home/',po.home,name='home'),
    path('poll/adm/',po.adm,name='course-view'),
    path('poll/poll_new_fees/',po.poll_fees,name='poll-new-fees'),
    path('poll/poll_new_data/',po.poll_data,name='poll-new-data'),
    
    

]
