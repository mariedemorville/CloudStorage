from django.contrib.auth import views
from django.urls import path

from .views import *
# from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', signup, name='signup'),
    path('profile/', redirect_user, name="profile"),
    path('all/', get_all_users, name="user_detail"),
]