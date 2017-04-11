from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from baseapp.models import Ingredient

class IngredientList(ListView):
    model = Ingredient
    template_name = "ingredient/list.html"

class IngredientDetail(DetailView):
     model = Ingredient
     template_name = "ingredient/detail.html"

class IngredientCreation(CreateView):
     model = Ingredient
     success_url = reverse_lazy('pizza:ingredient_list')
     fields = ['name', 'description']
     template_name = "ingredient/form.html"

class IngredientUpdate(UpdateView):
     model = Ingredient
     success_url = reverse_lazy('pizza:ingredient_list')
     fields = ['name', 'description', 'price']
     template_name = "ingredient/form.html"

class IngredientDelete(DeleteView):
     model = Ingredient
     success_url = reverse_lazy('pizza:ingredient_list')
     template_name = "ingredient/confirm_delete.html"
