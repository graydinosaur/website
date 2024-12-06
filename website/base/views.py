from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
	return render(request, "home.html", {})

def AuthView(request):
	form = UserCreationForm()
	return render(request,"registration/signup.html",{"form":form})