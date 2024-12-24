from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ContactUs
def home(request):
    return render(request, 'home.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new ContactUs instance and save it to the database
        contact = ContactUs(name=name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact_us')

    return render(request, 'skillrelay/contactus.html')
def dashboard(request):
    return render(request, 'dashboard.html')

# User Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful. Please login.")
        return redirect('login')

    return render(request, 'skillrelay/signup.html')


# User Login View
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'skillrelay/login.html')


# User Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def findwork(request):
    return render(request, 'findwork.html')
