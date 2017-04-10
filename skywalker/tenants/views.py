from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Tenant

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


class TenantCreation(CreateView):
    model = Tenant
    success_url = reverse_lazy('Tenants:list')
    fields = ['name', 'paid_until', 'on_trial']


class TenantUpdate(UpdateView):
    model = Tenant
    success_url = reverse_lazy('Tenants:list')
    fields = ['name', 'paid_until', 'on_trial']


class TenantDelete(DeleteView):
    model = Tenant
    success_url = reverse_lazy('Tenants:list')