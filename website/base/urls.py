from django.urls import path, include
from .views import AuthView, home
urlpatterns =  [    
    path("", home, name="home"),
    path("signup/", AuthView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]