# accounts/urls.py

from django.urls import path
from .views import *
from knox import views as knox_views
# from knox.views import LogoutView as knoxLogoutView

urlpatterns = [
    path('register/', register_user.as_view(), name='register'),
    path('login/', user_login.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logout'),

]