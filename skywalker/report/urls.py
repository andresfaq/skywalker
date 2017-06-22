from django.conf.urls import url

from report.views import (
    most_sold_ingredients,
    most_sold_pizzas,
    sale_by_employee,
)


urlpatterns = [
    url(r'^most_sold_ingredients/$', most_sold_ingredients, name='most_sold_ingredients'),
    url(r'^most_sold_pizzas/$',      most_sold_pizzas,      name='most_sold_pizzas'),
    url(r'^sale_by_employee/$',      sale_by_employee,      name='sale_by_employee'),

]