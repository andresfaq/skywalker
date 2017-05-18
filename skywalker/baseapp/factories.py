import factory
import factory.fuzzy
import datetime

from baseapp import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Employee Factory
class IngredientFactory(factory.Factory):
    class Meta:
        model = models.Ingredient

    name = factory.Sequence(lambda n: "Ingredient Name %03d" % n)
    description = factory.Faker('text', max_nb_chars=200)
    price = factory.fuzzy.FuzzyInteger(1000, 9999)

