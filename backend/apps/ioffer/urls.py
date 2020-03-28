from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test, name='index'),
    path('test_template/', views.test_template, name='test_template')
]
