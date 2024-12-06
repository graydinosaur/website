from django.urls import path, include
from .views import registerview, home
from . import views
urlpatterns =  [    
    path("", home, name="home"),
    path("signup/", registerview, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('dropdown/', views.dropdown_view, name='dropdown_view'),
]