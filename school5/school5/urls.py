"""school5 URL Configuration

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
from django.urls import path,include
from poll import views as poll_view
from app import views as app_view

# urlpatterns = [
    # path('admin/', admin.site.urls),
    # first aproch 
    # path('poll/',include('poll.urls')),
    # path('app/',include('app.urls')),
    # second aproch 
    # path('poll/',include([
    # path("home/cource/",poll_view.cource,name="cource-views"),
    # path("home/fees/",poll_view.fees,name="fees-views"),

    # ])),

    # path('app/',include([
    # path("app/sign_up",app_view.sign_up,name='sign-up'),
    # path("app/login",app_view.login,name='login'),

    # ])),

# ]
# poll_urll_pattern=[
#     path("home/cource/",poll_view.cource,name="cource-views"),
#     path("home/fees/",poll_view.fees,name="fees-views"),
# ]

# app_url_pattern=[
#      path("app/sign_up",app_view.sign_up,name='sign-up'),
#     path("app/login",app_view.login,name='login'),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('poll/', include.(poll_urll_pattern)),
#     path('app/', include.(app_url_pattern)),

# ]



