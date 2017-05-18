from django.db import connection
from tenant_schemas.utils import get_tenant_model

from baseapp.models import Ingredient
from baseapp.factories import IngredientFactory

# How to execute this seeders
# python manage.py shell < seeders.py --settings=skywalker.settings.dev

# Get the tenant // TODO: Create a function to get all the tenant list 
tenant = get_tenant_model().objects.get(schema_name='tenant')
# Set the tenant to be seeded
connection.set_tenant(tenant)


# ============================== ELIMINANDO INFORMACION PREVIA EN LA BD ============================== #
# Eliminando ventas
ingredient = Ingredient.objects.all()
for x in ingredient:
    x.delete()

print('DELETE COMPLETE')
# ============================== CREANDO INFORMACION NUEVA EN LA BD ============================== #

#Creando Ventas
for x in range(10):
	Ingredient.save(IngredientFactory.create())

print('CREATE COMPLETE')
