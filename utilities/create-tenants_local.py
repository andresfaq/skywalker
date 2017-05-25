# This script create a public and a private tenant for testing

from tenants.models import Tenant
tenant = Tenant(domain_url='localhost',
                schema_name='public',
                name='public',
                paid_until='2018-12-05',
                on_trial=False)
tenant.save()

tenant = Tenant(domain_url='tenant.localhost',
                schema_name='tenant',
                name='Tenant One',
                paid_until='2018-12-05',
                on_trial=True)
tenant.save()
