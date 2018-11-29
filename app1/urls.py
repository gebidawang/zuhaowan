"""django_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .views import *
urlpatterns = [
    path('login/', show_login, name='login'),
    path('regist/', show_regist, name='regist'),
    path('add_account/', add_request, name='add_C'),
    path('add_login/', add_login, name='login_e'),
    path('show_home/', show_home, name='show_home'),
    path('get_class/', get_classes, name='get_class'),
    path('add_stuinfor/', add_stuinfor, name='add_stuinfor'),
    path('add_scours/', add_scours, name='add_scours'),
    path('get_crouse/', get_crouse, name='get_crouse'),
    path('get_teaid/', get_teaid, name='get_teaid'),
    path('get_all_teachers/', get_all_teachers, name='get_all_teachers'),
    path('touch_score/', touch_score, name='touch_score'),
]
