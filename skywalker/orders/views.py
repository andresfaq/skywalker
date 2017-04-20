from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from baseapp.models import (
    Order,
    Ingredient,
    PizzaBase,
    Pizza
)

from baseapp.mixin import TitleContentPageMixin

from .forms import (
    OrderForm,
    IngredientForm,
    PizzaBaseForm,
    PizzaForm
)

# ENTITY ORDER
#products-view
class PizzaBaseproductsViewList(TitleContentPageMixin, ListView):
    model = PizzaBase
    template_name = "orders/products-view.html"
    title_content = "orders"

class OrderList(TitleContentPageMixin, ListView):
    model = Order
    template_name = "orders/list.html"
    title_content = "orders"

class OrderCreation(TitleContentPageMixin, SuccessMessageMixin, CreateView):
    model = Order
    #success_url = reverse_lazy('orders:order_list')
    form_class = OrderForm
    template_name = "object/object_form.html"
    success_message = "Order create successfully"
    title_content = "New Order"

    def get_context_data(self, **kwargs):
        context = super(OrderCreation, self).get_context_data(**kwargs)
        context['form_title'] = "Create an ingredient"
        return context

class OrderDelete(TitleContentPageMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order_list')
    template_name = "orders/confirm_delete.html"
    title_content = "Delete Ingredient"

class OrderUpdate(TitleContentPageMixin, SuccessMessageMixin, UpdateView):
    model = Order
    success_url = reverse_lazy('orders:order_list')
    form_class = OrderForm
    template_name = "object/object_form.html"
    success_message = "Order edit successfully"
    title_content = "Update Order"

    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context['form_title'] = "Edit an ingredient"
        return context

class OrderDetail(TitleContentPageMixin,DetailView):
    model = Order
    template_name = "orders/detail.html"
    title_content = "Detail Order"


# ENTITY INGREDIENT
class IngredientList(TitleContentPageMixin, ListView):
    model = Ingredient
    template_name = "ingredient/list.html"
    title_content = "Ingredients"

class IngredientDetail(TitleContentPageMixin,DetailView):
    model = Ingredient
    template_name = "ingredient/detail_1.html"
    title_content = "Detail Ingredient"

class IngredientCreation(TitleContentPageMixin, SuccessMessageMixin, CreateView):
    model = Ingredient
    success_url = reverse_lazy('pizza:ingredient_list')
    form_class = IngredientForm
    template_name = "object/object_form.html"
    success_message = "Ingredient create successfully"
    title_content = "New Ingredient"

    def get_context_data(self, **kwargs):
        context = super(IngredientCreation, self).get_context_data(**kwargs)
        context['form_title'] = "Create an ingredient"
        return context

class IngredientUpdate(TitleContentPageMixin, SuccessMessageMixin, UpdateView):
    model = Ingredient
    success_url = reverse_lazy('pizza:ingredient_list')
    form_class = IngredientForm
    template_name = "object/object_form.html"
    success_message = "Ingredient edit successfully"
    title_content = "Update Ingredient"

    def get_context_data(self, **kwargs):
        context = super(IngredientUpdate, self).get_context_data(**kwargs)
        context['form_title'] = "Edit an ingredient"
        return context

class IngredientDelete(TitleContentPageMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('pizza:ingredient_list')
    template_name = "ingredient/confirm_delete.html"
    title_content = "Delete Ingredient"

# ENTITY PIZZA BASE
class PizzaBaseList(TitleContentPageMixin,ListView):
    model = Pizza
    template_name = "orders/list_1.html"
    title_content = "Pizza List"

class PizzaBaseDetail(TitleContentPageMixin, DetailView):
    model = PizzaBase
    template_name = "orders/detail_1.html"
    title_content = "Detail Base Pizza"

class PizzaBaseCreation(TitleContentPageMixin, SuccessMessageMixin,CreateView):
    model = PizzaBase
    success_url = reverse_lazy('pizza:pizzabase_list')
    form_class = PizzaBaseForm
    template_name = "object/object_form.html"
    success_message = "Base Pizza create successfully"
    title_content = "New Base Pizza"

    def get_context_data(self, **kwargs):
        context = super(PizzaBaseCreation, self).get_context_data(**kwargs)
        context['form_title'] = "Create a pizza base"
        return context


class PizzaBaseUpdate(TitleContentPageMixin, SuccessMessageMixin,UpdateView):
    model = PizzaBase
    success_url = reverse_lazy('pizza:pizzabase_list')
    form_class = PizzaBaseForm
    template_name = "object/object_form.html"
    success_message = "Base Pizza edit successfully"
    title_content = "Update Base Pizza"

    def get_context_data(self, **kwargs):
        context = super(PizzaBaseUpdate, self).get_context_data(**kwargs)
        context['form_title'] = "Create a pizza base"
        return context


class PizzaBaseDelete(TitleContentPageMixin, DeleteView):
    model = PizzaBase
    success_url = reverse_lazy('pizza:pizzabase_list')
    template_name = "pizzaBase/confirm_delete.html"
    title_content = "Delete Base Pizza"

# ENTITY PIZZA
class PizzaList(TitleContentPageMixin,ListView):
    model = Pizza
    template_name = "pizza/list.html"
    title_content = "Pizzas"

class PizzaDetail(TitleContentPageMixin, DetailView):
    model = Pizza
    template_name = "pizza/detail.html"
    title_content = "Detail Pizza"

class PizzaCreation(TitleContentPageMixin, SuccessMessageMixin,CreateView):
    model = Pizza
    success_url = reverse_lazy('pizza:pizza_list')
    form_class = PizzaForm
    template_name = "object/object_form.html"
    success_message = "Pizza create successfully"
    title_content = "New Pizza"

    def get_context_data(self, **kwargs):
        context = super(PizzaCreation, self).get_context_data(**kwargs)
        context['form_title'] = "Create a pizza"
        return context


class PizzaUpdate(TitleContentPageMixin, SuccessMessageMixin,UpdateView):
    model = Pizza
    success_url = reverse_lazy('pizza:pizza_list')
    form_class = PizzaForm
    template_name = "object/object_form.html"
    success_message = "Pizza edit successfully"
    title_content = "Update Pizza"

    def get_context_data(self, **kwargs):
        context = super(PizzaUpdate, self).get_context_data(**kwargs)
        context['form_title'] = "Create a pizza"
        return context


class PizzaDelete(TitleContentPageMixin, DeleteView):
    model = Pizza
    success_url = reverse_lazy('pizza:pizza_list')
    template_name = "pizza/confirm_delete.html"
    title_content = "Delete Pizza"
