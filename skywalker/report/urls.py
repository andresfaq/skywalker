from django.conf.urls import url

from report.views import (
    most_sold_ingredients,
)


urlpatterns = [
    url(r'^most_sold_ingredients/$', most_sold_ingredients.as_view(), name='most_sold_ingredients'),
]