from django.contrib import admin
from baseapp import models

# Register your models here.

admin.site.register(models.Ingredient)
admin.site.register(models.PizzaBase)