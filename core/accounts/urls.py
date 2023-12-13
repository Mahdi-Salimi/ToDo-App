from django.urls import path, include
from .views import UserLogin, UserRegister
from django.contrib.auth.views import LogoutView


app_name = 'accounts'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),

]