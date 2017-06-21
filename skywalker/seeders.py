import random

from django.db import connection
from tenant_schemas.utils import get_tenant_model

from baseapp.models import Ingredient, PizzaBase, Pizza
from baseapp.factories import IngredientFactory, PizzaBaseFactory, PizzaFactory

# How to execute this seeders
# python manage.py shell < seeders.py --settings=skywalker.settings.dev

# Get the tenant // TODO: Create a function to get all the tenant list 
tenant = get_tenant_model().objects.get(schema_name='tenant')
# Set the tenant to be seeded
connection.set_tenant(tenant)

# ============================== UTILITIES ============================== #

# create a list of random model objects, this can be used to populate m2m relations
def getRandomModelList(model, n):
    count = model.objects.count()
    list = []
    for x in range(n):
        random_idx = random.randint(0, count - 1)
        list.append( model.objects.all()[random_idx] )
    return list

# ============================== ELIMINANDO INFORMACION PREVIA EN LA BD ============================== #

# ===== Eliminando Pizzas =====
print('\nDeleting Pizzas...')

pizza = Pizza.objects.all()
for x in pizza:
    x.delete()

print('\nDeleted!')

# ===== Eliminando Pizzas Base =====
print('\nDeleting PizzasBase...')

pizza_base = PizzaBase.objects.all()
for x in pizza_base:
    x.image.delete(save=False)
    x.delete()

print('\nDeleted!')

# ===== Eliminando Ingredientes =====
print('\nDeleting Ingredients...')

ingredient = Ingredient.objects.all()
for x in ingredient:
    x.delete()

print('\nDeleted!')

print('\nDELETE COMPLETE\n')

# ============================== CREANDO INFORMACION NUEVA EN LA BD ============================== #

# ===== Creando Ingredientes =====
print('\nCreating Ingredients...')

for x in range(10):
    Ingredient.save(IngredientFactory.create())

print('\nDone')

# ===== Creando PizzasBase =====
print('\nCreating PizzasBase...')

for x in range(10):
    ingredients = getRandomModelList(Ingredient, 3)
    PizzaBase.save(PizzaBaseFactory.create(aditions = ingredients))

print('\nDone')

# ===== Creando Pizza =====
print('\nCreating Pizzas...')

for x in range(10):
    Pizza.save(PizzaFactory.create())

print('\nDone')

print('CREATE COMPLETE')
