"""skywalker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from baseapp.views import index
from accounts.views import login_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^console/', include('baseapp.urls')),
    url(r'^pizza/', include('pizza.urls', namespace='pizza')),
    url(r'^tenant/', include('tenants.urls', namespace='tenants')),

    url(r'^$', index, name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('allauth.urls')),
]

## Se agregan este codigo para poder acceder a la imagen de la pizza que se encuentra
## en el directorio media/upload
# Django Tutorial for Beginners - 33 - Upload Files, https://www.youtube.com/watch?v=v5FWAxi5QqQ

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
