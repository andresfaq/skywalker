from django.conf.urls import url

from report.views import (
    most_sold_ingredients,
    most_sold_pizzas,
)


urlpatterns = [
    url(r'^most_sold_ingredients/$', most_sold_ingredients, name='most_sold_ingredients'),
    url(r'^most_sold_pizzas/$',      most_sold_pizzas,      name='most_sold_pizzas'),
]