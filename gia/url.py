from django.urls import path
from gia.views import *
from gia import views
from django.contrib.auth import views as wer

urlpatterns = [
    path('', index, name='index'),
    path('login/',wer.LoginView.as_view(template_name = 'gia/login.html'), name='login'),
    path('logaut/',wer.LogoutView.as_view(template_name = 'gia/logaut.html'), name='logaut'),
    path('register/', views.regist.as_view(), name='register'),
]