from django.conf.urls import url
from client.views import (
    index,
    order,
    order_create,
    order_cancel,
    history
)
from django.views.generic import TemplateView

urlpatterns = [
     url(r'^index/$', index, name='client_index'),
     url(r'^order/$', order, name='client_order'),
     url(r'^order/create/$', order_create, name='client_order_create'),
     url(r'^history/$', history, name='client_history'),
     url(r'^order/cancel/(?P<id>\d+)$', order_cancel, name='client_order_cancel'),
    
    # bryan: temporal
    url(r'^temp/$', TemplateView.as_view(template_name="client/base_purchases.html"), name='temp'),
]