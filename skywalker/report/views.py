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


def llenarDB ():
    #list_admitidos = lista_admitidos.objects.filter(carrera=carrera).order_by('-puntaje')[:cupos]
    #john = Author.objects.create(name="John")
    extra      = Extra()
    ingredient = Ingredient()
    order      = Order ()
    #pizzabase1  = PizzaBase.objects.get (name = "pizza1")

    #order.pizza       = Pizza.objects.get      (pk = 1)
    #order.ingredients.add (Ingredient.objects.get (pk = 1).id)
    #order.note        = "note1"

    ingredient1 = Ingredient.objects.get (pk = 2)
    order1 = Order.objects.create (pizza = Pizza.objects.get(pk = 2), note = "note2" )
    extra1 = Extra.objects.create (order      = order1, ingredient = ingredient1, amount     = 11 )

    #print ("extra1: "+ str (extra1.amount))

    #extra.order      = order1;
    #extra.ingredient = ingredient1;
    #extra.amount     = 2



