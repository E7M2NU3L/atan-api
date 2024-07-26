from django.urls import path
from user_authentication import views

urlpatterns = [
    path('login', views.login, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', views.logout, name="Logout"),
]