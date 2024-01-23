
from django.shortcuts import render, redirect
from .forms import OrderForm
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from dal import autocomplete
from .models import Product, Client, PlaceImpl, Car, PlaceFrom, Order


def IndexView(request):
    return render(request, 'home.html')


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            print(form.cleaned_data['product'])
            count = form.cleaned_data['count']
            product_title = form.cleaned_data['product']
            client_title = form.cleaned_data['client']
            place_impl_title = form.cleaned_data['placeImpl']
            car_number = form.cleaned_data['car']
            place_from_title = form.cleaned_data['placeFrom']

            product_instance, _ = Product.objects.get_or_create(title=product_title)
            client_instance, _ = Client.objects.get_or_create(title=client_title)
            place_impl_instance, _ = PlaceImpl.objects.get_or_create(title=place_impl_title)
            car_instance, _ = Car.objects.get_or_create(number=car_number)
            place_from_instance, _ = PlaceFrom.objects.get_or_create(title=place_from_title)

            order_instance = Order.objects.create(
                count=count,
                product=product_instance,
                client=client_instance,
                placeImpl=place_impl_instance,
                car=car_instance,
                placeFrom=place_from_instance,
            )

        return redirect('home')
    else:
        form = OrderForm()

    products = Product.objects.all()
    clients = Client.objects.all()
    placesImpl = PlaceImpl.objects.all()
    cars = Car.objects.all()
    placesFrom = PlaceFrom.objects.all()

    return render(request, 'orderAdd.html', {
        'form': form,
        'products': products,
        'clients': clients,
        'placesImpl': placesImpl,
        'cars': cars,
        'placesFrom': placesFrom,
    })


