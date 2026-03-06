# >---------------------------------------<
# (URL Configuration for Accounts) -------<
# >---------------------------------------<

from django.contrib.auth import views as auth_views

from django.urls import path
from accounts import views

# App namespace
app_name = "accounts"

# URL patterns for authentication
urlpatterns = [
    # User registration
    path("registry/", views.registry, name="registry"),
    
    # User login with custom template
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    
    # User logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]