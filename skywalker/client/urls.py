from django.conf.urls import url
from client.views import (
    index,
    order,
    order_create,
    order_cancel,
    history
)

urlpatterns = [
     url(r'^$', index, name='client_index'),
     url(r'^order/$', order, name='client_order'),
     url(r'^order/create/$', order_create, name='client_order_create'),
     url(r'^history/$', history, name='client_history'),
     url(r'^order/cancel/(?P<id>\d+)$', order_cancel, name='client_order_cancel'),
     
]