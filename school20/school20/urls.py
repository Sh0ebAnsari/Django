"""school20 URL Configuration

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
from poll import views
from enroll import views as session_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("set_cookie",views.set_cookie,name="set-cookie"),
    # path("get_cookie",views.get_cookie,name="get-cookie"),
    # path("del_cookie",views.del_cookie,name="del-cookie"),
    
    # path("set_signed_cookie",views.set_signed_cookie,name="set-signed-cookie"),
    # path("get_signed_cookie",views.get_signed_cookie,name="get-signed-cookie"),
    # path("del_signed_cookie",views.del_signed_cookie,name="del-signed-cookie"),
   

    # path("set_session",session_view.set_session,name="set-session"),
    # path("get_session",session_view.set_session,name="set-session"),
    # path("set_session",session_view.set_session,name="set-session"),
   

]
