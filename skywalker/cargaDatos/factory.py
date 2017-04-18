import factory
import factory.fuzzy
import datetime

# from administracion import models
from baseapp.models import (
    Ingredient,
    PizzaBase,
    Pizza,
)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#===================================================
#Generadores de Empleados
class PizzaBaseFactory(factory.Factory):
    class Meta:
        model = PizzaBase
    name = factory.Sequence(lambda n: "pizzaBase%03d" % n)
    description = factory.Faker('text', max_nb_chars=1200)
    image = "/media/upload/4439232-wolf-wallpapers.jpg"
    aditions = " "

