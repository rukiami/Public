from django.urls import path

from .import views

app_name="account"
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]  

# account/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 他のURLパターン
    path('calendar/', views.calendar_view, name='calendar'),
]
