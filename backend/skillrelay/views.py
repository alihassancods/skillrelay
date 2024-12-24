from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
def home(request):
    return render(request, 'skillrelay/home.html')
def profile_setup(request, user_type):
    if request.method == 'POST':
        if user_type == 'freelancer':
            form = FreelancerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                freelancer_profile = form.save(commit=False)
                freelancer_profile.user = request.user
                freelancer_profile.save()
                messages.success(request, "Freelancer profile setup successful!")
                return redirect('home')  # Redirect to the homepage or wherever you want
        elif user_type == 'employer':
            form = EmployerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                employer_profile = form.save(commit=False)
                employer_profile.user = request.user
                employer_profile.save()
                messages.success(request, "Employer profile setup successful!")
                return redirect('home')  # Redirect to the homepage or wherever you want
    else:
        if user_type == 'freelancer':
            form = FreelancerProfileForm()
        elif user_type == 'employer':
            form = EmployerProfileForm()

    return render(request, 'skillrelay/profile_setup.html', {'form': form, 'user_type': user_type})
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
        user_type = request.POST.get('user_type')  # Get the selected user type (Freelancer or Employer)

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

        # Redirect based on the user type (Freelancer or Employer)
        if user_type == 'freelancer':
            messages.success(request, "Signup successful. Please setup your Freelancer profile.")
            return redirect('profile_setup', user_type='freelancer')  # Redirect to the profile setup view with the user type
        elif user_type == 'employer':
            messages.success(request, "Signup successful. Please setup your Employer profile.")
            return redirect('profile_setup', user_type='employer')  # Redirect to the profile setup view with the user type

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

@login_required
def dashboard(request):
    # Try to fetch freelancer or employer profile based on the user's profile.
    try:
        freelancer_profile = FreelancerProfile.objects.get(user=request.user)
        is_freelancer = True
    except FreelancerProfile.DoesNotExist:
        is_freelancer = False
    
    try:
        employer_profile = EmployerProfile.objects.get(user=request.user)
        is_employer = True
    except EmployerProfile.DoesNotExist:
        is_employer = False

    # If the user is neither a freelancer nor an employer, handle accordingly (e.g., redirect or show a message)
    if not is_freelancer and not is_employer:
        return redirect('profile_setup')  # Redirect to profile setup page or any page that guides the user

    # If the user is a freelancer
    if is_freelancer:
        # Fetch freelancer's gigs
        gigs = Gig.objects.filter(freelancer=freelancer_profile)
        return render(request, 'skillrelay/freelancer-dashboard.html', {
            'user': request.user,
            'freelancer_profile': freelancer_profile,
            'gigs': gigs
        })
    
    # If the user is an employer
    if is_employer:
        # Fetch employer's posted projects
        projects = Project.objects.filter(employer=employer_profile)
        return render(request, 'skillrelay/client-dashboard.html', {
            'user': request.user,
            'employer_profile': employer_profile,
            'projects': projects
        })

    # If the user has no profile (should not reach here due to the check above)
    return redirect('profile_setup')