from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit \
    import (
    CreateView,
    UpdateView,
    DeleteView
)

from baseapp.models \
    import (
    Ingredient,
    PizzaBase
)


class IngredientList(ListView):
    model = Ingredient
    template_name = "ingredient/list.html"


class IngredientDetail(DetailView):
    model = Ingredient
    template_name = "ingredient/detail.html"


class IngredientCreation(CreateView):
    model = Ingredient
    success_url = reverse_lazy('pizza:ingredient_list')
    fields = ['name', 'description', 'price']
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


class PizzaBaseList(ListView):
    model = PizzaBase
    template_name = "pizzaBase/list.html"


class PizzaBaseDetail(DetailView):
    model = PizzaBase
    template_name = "pizzaBase/detail.html"


class PizzaBaseCreation(CreateView):
    model = PizzaBase
    success_url = reverse_lazy('pizza:pizzabase_list')
    fields = ['name', 'description', 'image', 'aditions']
    template_name = "pizzaBase/form.html"


class PizzaBaseUpdate(UpdateView):
    model = PizzaBase
    success_url = reverse_lazy('pizza:ingredient_list')
    fields = ['name', 'description', 'image']
    template_name = "pizzaBase/form.html"


class PizzaBaseDelete(DeleteView):
    model = PizzaBase
    success_url = reverse_lazy('pizza:pizzabase_list')
    template_name = "pizzaBase/confirm_delete.html"
