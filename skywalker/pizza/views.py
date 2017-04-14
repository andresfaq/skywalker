from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from baseapp.models import (
    Ingredient,
    PizzaBase
)

from .forms import IngredientForm



class IngredientList(ListView):
    model = Ingredient
    template_name = "ingredient/list.html"


class IngredientDetail(DetailView):
    model = Ingredient
    template_name = "ingredient/detail.html"


class IngredientCreation(SuccessMessageMixin, CreateView):
    model = Ingredient
    success_url = reverse_lazy('pizza:ingredient_list')
    form_class = IngredientForm
    template_name = "object/object_form.html"
    success_message = "Ingredient create successly"

    def get_context_data(self, **kwargs):
        context = super(IngredientCreation, self).get_context_data(**kwargs)
        context['form_title'] = "Create an ingredient"
        return context


class IngredientUpdate(UpdateView):
    model = Ingredient
    success_url = reverse_lazy('pizza:ingredient_list')
    form_class = IngredientForm
    template_name = "object/object_form.html"

    def get_context_data(self, **kwargs):
        context = super(IngredientUpdate, self).get_context_data(**kwargs)
        context['form_title'] = "Create an ingredient"
        return context


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
