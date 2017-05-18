from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Tenant
from .forms import TenantForm

# Create your views here.
class TenantList(ListView):
    model = Tenant
    extra_data = {}
    def get_context_data(self, **kwargs):
        context = super(TenantList, self).get_context_data(**kwargs)
        context.update(self.extra_data)
        return context


class TenantDetail(DetailView):
    model = Tenant
    extra_data = {}
    def get_context_data(self, **kwargs):
        context = super(TenantDetail, self).get_context_data(**kwargs)
        context.update(self.extra_data)
        return context


class TenantCreation(CreateView):
    model = Tenant
    success_url = reverse_lazy('tenants:list')
    form_class = TenantForm
    extra_data = {}
    def get_context_data(self, **kwargs):
        context = super(TenantCreation, self).get_context_data(**kwargs)
        context.update(self.extra_data)
        return context


class TenantUpdate(UpdateView):
    model = Tenant
    success_url = reverse_lazy('tenants:list')
    form_class = TenantForm
    extra_data = {}
    def get_context_data(self, **kwargs):
        context = super(TenantUpdate, self).get_context_data(**kwargs)
        context.update(self.extra_data)
        return context

class TenantDelete(DeleteView):
    model = Tenant
    success_url = reverse_lazy('tenants:list')
    extra_data = {}
    def get_context_data(self, **kwargs):
        context = super(TenantDelete, self).get_context_data(**kwargs)
        context.update(self.extra_data)
        return context