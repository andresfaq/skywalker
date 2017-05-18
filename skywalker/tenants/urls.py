from django.conf.urls import url
from tenants.views import (
    TenantList,
    TenantDetail,
    TenantCreation,
    TenantUpdate,
    TenantDelete
)

urlpatterns = [
    url(r'^$', TenantList.as_view( extra_data={'active':'list'} ), name='list'),
    url(r'^(?P<pk>\d+)$', TenantDetail.as_view(), name='detail'),
    url(r'^new', TenantCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', TenantUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', TenantDelete.as_view(), name='delete'),
]