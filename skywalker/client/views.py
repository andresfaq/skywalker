from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import Pizza
from datetime import datetime


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/index.html',{'pizzas': pizzas})
    
def order(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/order.html',{'pizzas': pizzas})
    
def order_create(request):
    if request.method == 'POST':
        pizzas_data =  request.POST.getlist('products_selected[]')
        i = 0
        pizzas = []
        sale = Sale(
            data = datetime.now()
        )
        for string in pizzas_data:
            identificator, quantity =  string.split('|')
            pizza = Pizza.objects.get(pk=1)
            i = i + 1
            sale.pizzas.add(pizza)
        sale.save()    
    return render(request, 'client/confirm.html',{'pizzas': pizzas})
    