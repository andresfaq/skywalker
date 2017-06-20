from django.shortcuts import render
from django.http import HttpResponse
from baseapp.models import Pizza, Sale, Order
from accounts.models import Employee, Client
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from datetime import datetime


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/index.html', {'pizzas': pizzas})

@login_required()
def order(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/order.html', {'pizzas': pizzas})

@login_required()
def order_create(request):
    if request.method == 'POST':
        client = Client.objects.get(id=request.user.id)  
        pizzas_data = request.POST.getlist('products_selected[]')
        sale_create = Sale(
            client=client,
            date=datetime.now()
        )
        sale_create.save()
        total_global = 0
        for string in pizzas_data:
            identificator, quantity_number = string.split('|')
            p = Pizza.objects.get(pk=identificator)
            total_order = p.price * float(quantity_number); 
            total_global += total_order
            order = Order(pizza=p, sale=sale_create, quantity=quantity_number, note="created by user", total=total_order)
            order.save()
            sale_create.order_set.add(order)
        sale_create.total = total_global
        sale_create.save()
    return render(request, 'client/confirm.html', {'sale': sale_create})



## vista usada para mostrar el historial de ventas
@login_required()
def history(request):
    client = Client.objects.get(id=request.user.id)  
    sales = Sale.objects.all().filter(client_id=client.id).order_by('-id');##TODO importante aqui se debe buscar por el cliente logueado
    return render(request, 'client/history.html', {'sales': sales})
    
@login_required()
def order_cancel(request, id):
    sale = Sale.objects.get(pk=id);
    sale.status = "CA";
    sale.save();
    sales = Sale.objects.all().filter().order_by('-id');##TODO importante aqui se debe buscar por el cliente logueado
    return render(request, 'client/history.html', {'sales': sales})
