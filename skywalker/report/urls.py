from django.conf.urls import url

from report.views import (
    most_sold_ingredients,
)


urlpatterns = [
    #url(r'^most_sold_ingredients/$', most_sold_ingredients.as_view(), name='most_sold_ingredients'),
    url(r'^most_sold_ingredients/$', most_sold_ingredients, name='most_sold_ingredients'),
    #url(r'^most_sold_ingredients_2/(?P<datos>.*)/(?P<datos_2>.*)$',most_sold_ingredients_2,name='most_sold_ingredients_2'),

]