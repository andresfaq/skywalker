from django.shortcuts import render, redirect
from baseapp.models import Pizza, Sale, Order

from django.contrib.auth.decorators import login_required


from datetime import datetime
from django.db import transaction

@login_required()
def order(request):
    pizzas = Pizza.objects.all()
    return render(request, 'order.html', {'pizzas': pizzas})
    
@login_required()
def sales(request):
    sales = Sale.objects.all().filter().order_by('-id');##TODO importante aqui se debe buscar por el cliente logueado
    return render(request, 'sales.html', {'sales': sales})
    
def sale_cancel(request, id):
    sale = Sale.objects.get(pk=id);
    sale.status = "CA";
    sale.save();
    return redirect('sale:sale_sales')    
    
def sale_approve(request, id):
    sale = Sale.objects.get(pk=id);
    sale.status = "DO";
    sale.save();
    return redirect('sale:sale_sales')
    
@transaction.atomic
def sale_order_create(request):
    if request.method == 'POST':
        pizzas_data = request.POST.getlist('products_selected[]')
        sale_create = Sale(
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
    return redirect('sale:sale_order')
