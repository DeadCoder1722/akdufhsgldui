"""hospital_appointment_and_information_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from hospital import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('dash/',views.dash_view,name='dashboard.html'),
    path('bookapp/',views.bookapp_view,name='bookapp.html'),
    path('calladoc/',views.calladoc_view,name='calladoc.html'),
    path('feedback/',views.feedback_view,name='feedback.html'),
    path('medicalreport/',views.medicalreport_view,name='medicalreport.html'),
    path('profile/',views.profile_view,name='profile.html'),
    path('yourhealth/',views.yourhealth_view,name='yourhealth.html'),
    path('home/',views.home_view,name='home.html'),
    path('services/',views.services_view,name='services.html'),
    path('contactus/',views.contactus_view,name='contactus.html'),
    path('news/',views.news_view,name='news.html'),
    path('login/',views.login_view,name='login.html'),
    #path('hospital/', include('hospital.urls')),
    
]
