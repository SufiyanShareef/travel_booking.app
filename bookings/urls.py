from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'bookings'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='bookings/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bookings/logout.html'),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('travel/', views.travel_list, name='travel-list'),
    path('booking/new/<int:travel_id>/', views.bookings_create, name='booking-create'),
    path('bookings/', views.booking_list, name='booking-list'),
    path('booking/cancel/<int:booking_id>/', views.booking_cancel, name='booking-cancel'),
]