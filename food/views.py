from django.shortcuts import render
from .models import Category, Menu, Events, Testimonials, Gallery, Chefs
from .forms import ReservationForm, ContactForm

def IndexView(request):
    foods = Menu.objects.all()

    print(foods)
    categories = Category.objects.all()
    events = Events.objects.all()

    reservation = ReservationForm()
    contact = ContactForm()

    testimonials = Testimonials.objects.all()
    gallery = Gallery.objects.all()
    chefs = Chefs.objects.all()

    context = {
        'foods': foods,
        'categories': categories,
        'events' : events,
        'reservation' : reservation,
        'contact' : contact,
        'testimonials' : testimonials,
        'gallery' : gallery,
        'chefs' : chefs,
    }

    return render(request, 'index.html', context)
