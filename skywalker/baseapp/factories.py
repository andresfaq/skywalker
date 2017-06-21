import factory
import factory.fuzzy
import datetime

from baseapp import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Ingredient Factory
class IngredientFactory(factory.Factory):
    class Meta:
        model = models.Ingredient

    name = factory.Sequence(lambda n: "Ingredient Name %03d" % n)
    description = factory.Faker('text', max_nb_chars=200)
    price = factory.fuzzy.FuzzyInteger(1000, 9999)


# PizzaBase Factory
class PizzaBaseFactory(factory.Factory):
    class Meta:
        model = models.PizzaBase

    name = factory.Sequence(lambda n: "PizzaBase Name %03d" % n)
    description = factory.Faker('text', max_nb_chars=200)
    image = factory.django.ImageField(filename=factory.Sequence(lambda n: "PizzaBaseImage %02d" % n),color='green',format='JPEG')
    
    @factory.post_generation
    def aditions(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of ingredient were passed in, use them
            for ingredient in extracted:
                self.aditions.add(ingredient)

