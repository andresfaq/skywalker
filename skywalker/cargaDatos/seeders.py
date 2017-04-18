# from django.contrib.auth.models import Group, Permission

from cargaDatos.factory import PizzaBaseFactory
from baseapp.models import (
    Ingredient,
    PizzaBase,
    Pizza,
)

print (PizzaBaseFactory.create())