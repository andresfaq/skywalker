from django.conf.urls import url

from report.views import (
    mostSoldExtraIngredients,
)


urlpatterns = [
    url(r'^mostSoldExtraIngredients/$', mostSoldExtraIngredients.as_view(), name='mostSoldExtraIngredients'),
]