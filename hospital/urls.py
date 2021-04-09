from django.contrib import admin
from django.urls import include, path
from hospital import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('dash_pat/',views.dash_view,name='dashboard.html'),
    path('bookapp_pat/',views.bookapp_view,name='bookapp.html'),
    path('calladoc_pat/',views.calladoc_view,name='calladoc.html'),
    path('feedback_pat/',views.feedback_view,name='feedback.html'),
    path('medicalreport_pat/',views.medicalreport_view,name='medicalreport.html'),
    path('profile_pat/',views.profile_pat_view,name='profile_pat.html'),
    path('yourhealth_pat/',views.yourhealth_view,name='yourhealth.html'),
    path('register_pat/',views.register_pat_view,name='register_pat.html'),
    path('login_pat/',views.login_pat_view,name='login_pat.html'),
    path('home/',views.home_view,name='home.html'),
    path('dash_doc/',views.dash_doc_view,name='dashboard_doc.html'),
    path('bookapp_doc/',views.bookapp_doc_view,name='bookapp_doc.html'),
    path('calladoc_doc/',views.calladoc_doc_view,name='calladoc_doc.html'),
    path('feedback_doc/',views.feedback_doc_view,name='feedback_doc.html'),
    path('register_doc/',views.register_doc_view,name='register_doc.html'),
    path('login_doc/',views.login_doc_view,name='login_doc.html'),
    path('medicalreport_doc/',views.medicalreport_doc_view,name='medicalreport_doc.html'),
    path('profile_doc/',views.profile_doc_view,name='profile_doc.html'),
    path('yourhealth_doc/',views.yourhealth_doc_view,name='yourhealth_doc.html'),
    path('dash_adm/',views.dash_adm_view,name='dashboard_adm.html'),
    path('bookapp_adm/',views.bookapp_adm_view,name='bookapp_adm.html'),
    path('calladoc_adm/',views.calladoc_adm_view,name='calladoc_adm.html'),
    path('medicalreport_adm/',views.medicalreport_adm_view,name='medicalreport_adm.html'),
    path('profile_adm/',views.profile_adm_view,name='profile_adm.html'),
    path('register_adm/',views.register_adm_view,name='register_adm.html'),
    path('login_adm/',views.login_adm_view,name='login_adm.html'),
    path('yourhealth_adm/',views.yourhealth_adm_view,name='yourhealth_adm.html'),
    path('home/',views.home_view,name='home.html'),
    path('login/',views.login_view,name='login.html'),
    path('bill/',views.bill_view,name='bill.html'),
    path('logout/',auth_views.LogoutView.as_view(template_name='hospital/logout.html'),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='hospital/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='hospital/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='hospital/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='hospital/password_reset_complete.html'),name='password_reset_complete'),
    #path('hospital/', include('hospital.urls')),
    
    
]