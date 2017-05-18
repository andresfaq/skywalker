from django.test import TestCase

from .models import Tenant

class AnimalTestCase(TestCase):
    def setUp(self):
        Tenant.objects.create(domain_url='tenant.skywalker-dev-andresfaq.c9users.io',
                schema_name='tenant_ci',
                name='Tenant CI',
                paid_until='2018-12-05',
                on_trial=False,
                style='smart-style-5')


    def test_tenant_has_schema_name(self):

        tenant = Tenant.objects.get(name="Tenant CI")
        self.assertEqual(tenant.on_trial, False)
