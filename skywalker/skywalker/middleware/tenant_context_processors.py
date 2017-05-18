from tenant_schemas.utils import get_tenant_model
from django.db import connection

def tenant_template_style(request):
    # Getting the current schema
    connection_schema = connection.schema_name
    tenant = get_tenant_model().objects.get(schema_name=connection_schema)
    context = {'style': tenant.style}
    if tenant.on_trial == True:
        context['style'] = 'smart-style-1'
        
    return context