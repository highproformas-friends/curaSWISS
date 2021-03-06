from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

from . import generate_users

urlpatterns = [
    # uncomment for data generation
    #path('add_data',generate_users.populate_db),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done_.html'),name='password_change_done'),
    path('password_change',auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form_.html'),name='password_change_form'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form_.html', from_email=settings.NOREPLY_MAIL),name='password_reset_form'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done_.html'),name='password_reset_done'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_.html'),name='password_reset_complete_'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm_.html',
        post_reset_login=True,
        success_url='/accounts/validate_email'
      ) , name='password_reset_confirm_'),
    path('login/', views.CustomLoginView.as_view(template_name='registration/login.html'),name='login'),
    path('', include('django.contrib.auth.urls')),
    path('validate_email', views.validate_email, name='validate_email'),
    path('profile_redirect', views.profile_redirect, name='profile_redirect'),
    path('login_redirect', views.login_redirect, name='login_redirect'),
    path('delete_me_ask', views.delete_me_ask, name='delete_me_ask'),
    path('delete_me', views.delete_me, name='delete_me'),
    path('signup_student', views.student_signup, name='student_signup'),
    path('signup_hospital', views.hospital_signup, name='hospital_signup'),
    path('profile_student', views.edit_student_profile, name='edit_student_profile'),
    path('profile_hospital', views.edit_hospital_profile, name='edit_hospital_profile'),
    path('approve_hospitals', views.approve_hospitals, name='approve_hospitals'),
    path('change_hospital_approval/<str:uuid>/', views.change_hospital_approval, name='change_hospital_approval')
]
