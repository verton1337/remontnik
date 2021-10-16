from django.urls import path
import authapp.views as authapp


urlpatterns = [
    path("", authapp.LoginView.as_view(), name="login"),
    path("logout/", authapp.LogoutView.as_view(), name="logout"),
]
