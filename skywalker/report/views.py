from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from baseapp.models import (
    Ingredient,
    Sale,
    PizzaBase,
    Pizza
)

from baseapp.mixin import TitleContentPageMixin

def most_sold_pizzas (request):
    template_name = "reports/most_sold_pizzas.html"

    consulta = Order.objects.values('pizza__pizza_base__name')\
        .annotate(count_pizzabase = Count('pizza__pizza_base__name'))\
        .order_by('-count_pizzabase')

    ctx = {'consulta': consulta}
    return render(request, template_name, ctx)







