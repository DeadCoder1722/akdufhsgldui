from django.contrib import admin
from django.urls import include, path
from hospital import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('bookapp_pat/',views.bookapp_view,name='bookapp.html'),
    path('calladoc_pat/',views.calladoc_view,name='calladoc.html'),
    path('feedback_pat/',views.feedback_view,name='feedback.html'),
    path('medicalreport_pat/',views.medicalreport_view,name='medicalreport.html'),
    path('admit_details_pat/',views.admit_details_view,name='admit_details.html'),
    path('admit_details/<int:pk>',views.admit_details_particular_view,name='admit_details_particular.html'),
    path('bookapp_details_pat/<int:pk>',views.appointment_details_particular_pat_view,name='bookapp_details_particular_pat.html'),
    path('endappointment_doc/<int:pk>',views.endappointment_doc_view,name='endappointment_doc'),
    path('profile_pat/',views.profile_pat_view,name='profile_pat.html'),
    path('yourhealth_pat/',views.yourhealth_view,name='yourhealth.html'),
    path('edityourhealth_pat/',views.edityourhealth_view,name='edityourhealth.html'),
    path('register_pat/',views.register_pat_view,name='register_pat.html'),
    path('login_pat/',views.login_pat_view,name='login_pat.html'),
    path('home/',views.home_view,name='home.html'),
    path('dash_doc/',views.dash_doc_view,name='dashboard_doc.html'),
    path('dash_doc/<int:pk>',views.dash_doc_approve_view,name='dashboard_doc_approve'),
    path('admit_details_doc/',views.admit_details_doc_view,name='admit_details_doc.html'),
    path('admit_details_doc/<int:pk>',views.admit_details_particular_doc_view,name='admit_details_particular_doc.html'),
    path('admit_details_doc/<int:pk>/<str:comm>/<int:quan>',views.admit_details_particular_doc_add_charge_view,name='admit_details_particular_doc_add_charge'),
    path('discharge_doc/<int:pk>',views.discharge_doc_view,name='discharge_doc'),
    path('bookapp_doc/',views.bookapp_doc_view,name='bookapp_doc.html'),
    path('bookapp_doc/<int:pk>/<str:date>/<str:time>/<str:link>',views.bookapp_doc_link_view,name='add_link'),
    path('bookapp_doc/<int:pk>',views.appointment_details_particular_doc_view,name='bookapp_details_particular_doc.html'),
    path('feedback_doc/',views.feedback_doc_view,name='feedback_doc.html'),
    path('register_doc/',views.register_doc_view,name='register_doc.html'),
    path('login_doc/',views.login_doc_view,name='login_doc.html'),
    path('profile_doc/',views.profile_doc_view,name='profile_doc.html'),
    path('dash_adm/',views.dash_adm_view,name='dashboard_adm.html'),
    path('patient_adm/',views.patient_adm_view,name='patient_adm.html'),
    path('doctor_adm/',views.doctor_adm_view,name='doctor_adm.html'),
    path('approve_pat/',views.approve_pat_view,name='approve_pat.html'),
    path('approve_doc/',views.approve_doc_view,name='approve_doc.html'),
    path('approve_doc/<int:pk>', views.approve_doctor_view,name='approve_doctor'),
    path('approve_pat/<int:pk>', views.approve_patient_view,name='approve_patient'),
    path('bookapp_adm/',views.bookapp_adm_view,name='bookapp_adm.html'),
    path('admit_adm/',views.admit_adm_view,name='admit_adm.html'),
    path('calladoc_adm/',views.calladoc_adm_view,name='calladoc_adm.html'),
    path('medicalreport_adm/',views.medicalreport_adm_view,name='medicalreport_adm.html'),
    path('profile_adm/',views.profile_adm_view,name='profile_adm.html'),
    path('admin_adm/',views.admin_adm_view,name='admin_adm.html'),
    path('register_adm/',views.register_adm_view,name='register_adm.html'),
    path('login_adm/',views.login_adm_view,name='login_adm.html'),
    path('yourhealth_adm/',views.yourhealth_adm_view,name='yourhealth_adm.html'),
    path('admin_appointment_view',views.admin_appointment_view,name='appoint_view_adm.html'),
    path('appointment_particular_adm/<int:pk>',views.appointment_particular_adm_view,name='appoint_particular_adm.html'),
    path('admin_admit_view',views.admin_admit_view,name='admit_view_adm.html'),
    path('admin_admit_view/<int:pk>',views.admit_particular_adm_view,name='admit_particular_adm.html'),
    path('pat_appointment_view',views.pat_appointment_view,name='appoint_view_pat.html'),
    path('home/',views.home_view,name='home.html'),
    path('login/',views.login_view,name='login.html'),
    path('bill/<int:pk>',views.bill_view,name='bill.html'),
    path('bill_apt/<int:pk>',views.bill_apt_view,name='bill_apt.html'),
    path('logout/',auth_views.LogoutView.as_view(template_name='hospital/logout.html'),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='hospital/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='hospital/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='hospital/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='hospital/password_reset_complete.html'),name='password_reset_complete'),
    path('approve_appoint', views.approve_appoint_view,name='approve_appoint.html'),
    path('approve_appoint/<int:pk>', views.approve_app_view,name='approve_app'),
    path('patient_all_view', views.patient_all_view,name='patient_all_view.html'),
    path('doctor_all_view', views.doctor_all_view,name='doctor_all_view.html'),
    path('admin_all_view', views.admin_all_view,name='admin_all_view.html'),
    path('report/<int:pk>',views.report_view,name='report.html'),
    path('report_apt/<int:pk>',views.report_apt_view,name='report_apt.html'),
    path('opcost',views.opcost_adm_view,name='opcost.html'),
    #path('hospital/', include('hospital.urls')),
    
    
    
]