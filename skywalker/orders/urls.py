from django.conf.urls import url
from orders.views import (
    OrderList,
    OrderCreation,
    OrderDelete,
    OrderUpdate,
    OrderDetail,
     IngredientList,
     IngredientDetail,
     IngredientCreation,
     IngredientUpdate,
     IngredientDelete,
     PizzaBaseList,
     PizzaBaseDetail,
     PizzaBaseCreation,
     PizzaBaseUpdate,
     PizzaBaseDelete,
     PizzaList,
     PizzaDetail,
     PizzaCreation,
     PizzaUpdate,
     PizzaDelete,
)

urlpatterns = [

    url(r'^ingredient/$', IngredientList.as_view(), name='ingredient_list'),
    url(r'^ingredient/(?P<pk>\d+)$', IngredientDetail.as_view(), name='ingredient_detail'),
    url(r'^ingredient/new$', IngredientCreation.as_view(), name='ingredient_creation'),
    url(r'^ingredient/edit/(?P<pk>\d+)$', IngredientUpdate.as_view(), name='ingredient_edit'),
    url(r'^ingredient/delete/(?P<pk>\d+)$', IngredientDelete.as_view(), name='ingredient_delete'),

    url(r'^order/$',                   OrderList.as_view(),       name='order_list'),
    url(r'^order/new$',                OrderCreation.as_view(),   name='order_creation'),
    url(r'^order/delete/(?P<pk>\d+)$', OrderDelete.as_view(),     name='order_delete'),
    url(r'^order/edit/(?P<pk>\d+)$',   OrderUpdate.as_view(),     name='order_edit'),
    url(r'^order/(?P<pk>\d+)$',        OrderDetail.as_view(),     name='order_detail'),


    url(r'^pizza-base-list/$', PizzaBaseList.as_view(), name='pizzabase_list'),
    url(r'^pizza-base-list/(?P<pk>\d+)$', PizzaBaseDetail.as_view(), name='pizzabase_detail'),
    url(r'^pizza-base/new$', PizzaBaseCreation.as_view(), name='pizzabase_creation'),
    url(r'^pizza-base/edit/(?P<pk>\d+)$', PizzaBaseUpdate.as_view(), name='pizzabase_edit'),
    url(r'^pizza-base/delete/(?P<pk>\d+)$', PizzaBaseDelete.as_view(), name='pizzabase_delete'),

    url(r'^pizza/$', PizzaList.as_view(), name='pizza_list'),
    url(r'^pizza/(?P<pk>\d+)$', PizzaDetail.as_view(), name='pizza_detail'),
    url(r'^pizza/new$', PizzaCreation.as_view(), name='pizza_creation'),
    url(r'^pizza/edit/(?P<pk>\d+)$', PizzaUpdate.as_view(), name='pizza_edit'),
    url(r'^pizza/delete/(?P<pk>\d+)$', PizzaDelete.as_view(), name='pizza_delete'),
]