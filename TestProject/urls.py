"""
URL configuration for TestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('javatest/', views.javatest),
    path('pythontest/', views.pythontest),
    path('aptitudetest/', views.aptitudetest),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view),
    path('signup/',views.signup),
    path('py_exam/',views.py_exam),
    path('java_exam/',views.java_exam),
    path('apt_exam/',views.aptitude_exam),
    path('verify_otp/', views.verify_otp, name='verify_otp'),

]

