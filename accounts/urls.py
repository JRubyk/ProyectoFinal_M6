from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register_view, dashboard_view

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
