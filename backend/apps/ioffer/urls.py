from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('thanks/', views.thanks, name='thanks'),
    path('ajax-functions/', views.load_functions, name='ajax-functions')
]
