from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('findwork/', views.findwork, name='findwork'),
    path('profile-setup/<str:user_type>/', views.profile_setup, name='profile_setup'),
]