from django.conf.urls import url
from client.views import (
    index,
)

urlpatterns = [
     url(r'^$', index, name='client_index'),
]