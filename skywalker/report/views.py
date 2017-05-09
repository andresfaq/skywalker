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
    PizzaBase,
    Pizza
)

from baseapp.mixin import TitleContentPageMixin

# REPORT
class mostSoldExtraIngredients(TitleContentPageMixin, ListView):
    model = Ingredient
    var1 = "contexto variable julian"
    template_name = "reports/mostSoldExtraIngredients.html"
    title_content = "Most Sold Extra Ingredients"

