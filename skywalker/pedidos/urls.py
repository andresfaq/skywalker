from django.conf.urls import url
from pizza.views import (
     IngredientList,
     IngredientDetail,
     IngredientCreation,
     IngredientUpdate,
     IngredientDelete,
)

urlpatterns = [
    url(r'^pizzalist/$', IngredientList.as_view(), name='ingredient_list'),
    url(r'^ingredient/(?P<pk>\d+)$', IngredientDetail.as_view(), name='ingredient_detail'),
    url(r'^ingredient/new$', IngredientCreation.as_view(), name='ingredient_creation'),
    url(r'^ingredient/edit/(?P<pk>\d+)$', IngredientUpdate.as_view(), name='ingredient_edit'),
    url(r'^ingredient/delete/(?P<pk>\d+)$', IngredientDelete.as_view(), name='ingredient_delete'),
]