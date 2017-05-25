from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import Pizza, Sale
from accounts.models import Employee, Client

from datetime import datetime


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/index.html', {'pizzas': pizzas})


def order(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/order.html', {'pizzas': pizzas})


def order_create(request):
    if request.method == 'POST':
        pizzas_data = request.POST.getlist('products_selected[]')
        client_db = Client.objects.get(pk=1)
        sale = Sale(
            client=client_db,
            date=datetime.now()
        )
        sale.save()
        for string in pizzas_data:
            identificator, quantity = string.split('|')
            pizza = Pizza.objects.get(pk=identificator)
            sale.pizzas.add(pizza)
        sale.save()
    return render(request, 'client/confirm.html', {'sale': sale})
