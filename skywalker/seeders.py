import factory
import factory.fuzzy
from django.db import connection
from tenant_schemas.utils import get_tenant_model

from baseapp.models import Ingredient, PizzaBase
from baseapp.factories import IngredientFactory, PizzaBaseFactory

# How to execute this seeders
# python manage.py shell < seeders.py --settings=skywalker.settings.dev

# Get the tenant // TODO: Create a function to get all the tenant list 
tenant = get_tenant_model().objects.get(schema_name='tenant')
# Set the tenant to be seeded
connection.set_tenant(tenant)


# ============================== ELIMINANDO INFORMACION PREVIA EN LA BD ============================== #
# Eliminando Pizzas Base
pizzaBase = PizzaBase.objects.all()
for x in pizzaBase:
    x.delete()

# Eliminando Ingredientes
ingredient = Ingredient.objects.all()
for x in ingredient:
    x.delete()

print('DELETE COMPLETE')
# ============================== CREANDO INFORMACION NUEVA EN LA BD ============================== #

#Creando Ingredientes
for x in range(10):
    Ingredient.save(IngredientFactory.create())

#Creando PizzasBase
for x in range(10):
    #ingredient1 = factory.fuzzy.FuzzyChoice(Ingredient.objects.all())
    #ingredient2 = factory.fuzzy.FuzzyChoice(Ingredient.objects.all())
    #ingredient3 = factory.fuzzy.FuzzyChoice(Ingredient.objects.all())
    #PizzaBase.save(PizzaBaseFactory.create(aditions=(ingredient1, ingredient2, ingredient3)))
    PizzaBase.save(PizzaBaseFactory.create())


print('CREATE COMPLETE')
