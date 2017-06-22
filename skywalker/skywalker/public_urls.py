from django.conf.urls import url, include
from django.views.generic import TemplateView

from django.contrib import admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^tenant/', include('tenants.urls', namespace='tenants')),
    
]
