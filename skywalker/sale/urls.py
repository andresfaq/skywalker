from django.conf.urls import url
from sale.views import (
    order,
    sales,
    sale_cancel,
    sale_approve,
    sale_order_create
)
from django.views.generic import TemplateView

urlpatterns = [
     url(r'^order/$', order, name='sale_order'),
     url(r'^sales/$', sales, name='sale_sales'),
     url(r'^sale/cancel/(?P<id>\d+)$', sale_cancel, name='sale_cancel'),
     url(r'^sale/approve/(?P<id>\d+)$', sale_approve, name='sale_approve'),
     url(r'^sale/order-create$', sale_order_create, name='sale_order_create'),

]