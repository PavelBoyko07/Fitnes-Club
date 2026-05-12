from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import register_view, login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', register_view, name='logout'),
    path('register/', register_view, name='register')
]
