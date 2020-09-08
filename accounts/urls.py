from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
