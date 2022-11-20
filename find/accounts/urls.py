from django.urls import path
from .views import registration_view, update_profile_view, view_profile_view, LoginView

urlpatterns = [
    path("register/", registration_view, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", view_profile_view, name="view"),
    path("profile/update", update_profile_view, name="update"),
]
