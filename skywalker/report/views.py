from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from baseapp.models import (
    Ingredient,
    Extra,
    Order,
    Sale,
    PizzaBase,
    Pizza
)

from baseapp.mixin import TitleContentPageMixin

# REPORT
def most_sold_ingredients(request):
    model = Ingredient
    template_name = "reports/most_sold_ingredients.html"
    title_content = "Most Sold Extra Ingredients"

    consulta = Extra.objects.values('ingredient__name')\
        .annotate(ingredient_amount=Sum('amount'))\
        .order_by('ingredient')

    ctx = {'consulta': consulta}
    return render(request, template_name, ctx)






