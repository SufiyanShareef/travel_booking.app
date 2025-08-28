from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .forms import UserRegisterForm, UseeUpdateForm, ProfileUpdateForm
from .models import TravelOption, Booking


# Create your views here.

def home(request):
    return render(request,'bookings/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account cretaed for {username}! You can now log in')
            return redirect('bookings:login')
    else:
            form = UserRegisterForm()
    return render(request, 'bookings/register.html', {'form': form})

def travel_list(request):
    travel_options = TravelOption.objects.all()
    # all_travel_options = TravelOption.objects.all()
    # print(f"DEBUG: All travel options count: {all_travel_options.count()}")

    travel_type = request.GET.get('type')
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')

    if travel_type:
        travel_options = travel_options.filter(type=travel_type)
    if source:
        travel_options = travel_options.filter(source=source)
    if destination:
        travel_options = travel_options.filter(destination=destination)
    if date:
        travel_options = travel_options.filter(date=date)

    # print(f"DEBUG: Travel options query: {travel_options.query}")
    # print(f"DEBUG: Found {travel_options.count()} travel options")
    # for travel in travel_options:
    #     print(f"DEBUG: {travel.source} to {travel.destination}")

    context = {
        'travel_options': travel_options,
        'TRAVEL_TYPES': TravelOption.TRAVEL_TYPES,
        'selected_type': travel_type,
        'selected_source': source,
        'selected_destination': destination,
        'selected_date': date,
    }

    return render(request, 'bookings/travel_list.html', context)




@login_required
def profile(request):
    print(f"[DEBUG] Method: {request.method}")
    if request.method == 'POST':
        user_form = UseeUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('bookings:profile')
    else:
        print("[DEBUG] Handling GET")
        user_form = UseeUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'bookings/profile.html', context)

@login_required
def bookings_create(request, travel_id):
    travel_options = get_object_or_404(TravelOption,id=travel_id)
    # print(travel_options)
    if request.method == 'POST':
        number_of_seats = int(request.POST.get('number_of_seats', 1))

        if number_of_seats <= 0:
            messages.error(request, 'Number of seats must be at least 1.')
        elif number_of_seats > travel_options.available_seats:
            messages.error(request, f'Only {travel_options.available_seats} seats available ')
        else :
            total_price = travel_options.price * number_of_seats 
            booking = Booking(
                user = request.user,
                travel_option= travel_options,
                number_of_seats = number_of_seats,
                total_price = total_price,
                status = Booking.CONFIRMED
            )
            booking.save()

            travel_options.available_seats -= number_of_seats
            travel_options.save()

            messages.success(request, 'Bookings confirmed1')
            return redirect('bookings:booking-list')
    context = {'travel_options': travel_options}
    return render(request, 'bookings/booking_form.html', context)

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    context = {'bookings': bookings}
    return render(request,'bookings/booking_list.html', context)

@login_required
def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status == Booking.CONFIRMED:
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        booking.status = Booking.CANCELLED
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.warning(request, 'Booking is already cancelled.')
    return redirect('bookings:booking-list')



