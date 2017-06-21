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
    # Extra,
    Order,
    Sale,
    PizzaBase,
    Pizza
)

from baseapp.mixin import TitleContentPageMixin

def most_sold_pizzas (request):
    template_name = "reports/most_sold_pizzas.html"

    # la consulta hace join de: order con pizza con pizza_base los
    # __ significa join o seleccionar una columna
    # annotate son funciones extra que se le puede meter a la consulta como : Sum y Count
    # -count_pizzabase: ordenar de forma descendente
    consulta = Order.objects.values('pizza__pizza_base__name')\
        .annotate(count_pizzabase = Count('pizza__pizza_base__name'))\
        .order_by('-count_pizzabase')

    ctx = {'consulta': consulta}
    return render(request, template_name, ctx)

# REPORT
def most_sold_ingredients(request):
    model = Ingredient
    template_name = "reports/most_sold_ingredients.html"
    title_content = "Most Sold Extra Ingredients"
    """
    consulta = Extra.objects.values('ingredient__name')\
        .annotate(ingredient_amount=Sum('amount'))\
        .order_by('ingredient')
        """
    """
    consulta = Extra.objects.values('ingredient__name')\
        .annotate(ingredient_amount=Sum('amount'))\
        .order_by('-ingredient_amount')"""
    consulta = ""

    ctx = {'consulta': consulta}
    return render(request, template_name, ctx)






