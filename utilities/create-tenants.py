# This script create a public and a private tenant for testing

from tenants.models import Tenant
tenant = Tenant(domain_url='skywalker-dev-andresfaq.c9users.io',
                schema_name='public',
                name='public',
                paid_until='2018-12-05',
                on_trial=False,
                style='smart-style-5')
tenant.save()

tenant = Tenant(domain_url='tenant.skywalker-dev-andresfaq.c9users.io',
                schema_name='tenant',
                name='Tenant One',
                paid_until='2018-12-05',
                on_trial=True,
                style='smart-style-6')
tenant.save()
