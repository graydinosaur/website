from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Home view that requires the user to be logged in
@login_required
def home(request):
    return render(request, "home.html", {})

# Auth view for handling user registration
def registerview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Corrected: form.save() with parentheses to actually save the user
            return redirect('accounts/login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

def dropdown_view(request):
    links = [
        {"name": "Link 1", "url": "#"},
        {"name": "Link 2", "url": "#"},
        {"name": "Link 3", "url": "#"},
    ]
    return render(request, 'dropdown_template.html', {'links': links})
