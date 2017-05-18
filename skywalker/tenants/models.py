from django.db import models
from tenant_schemas.models import TenantMixin
# Create your models here.

class Tenant(TenantMixin):
    SMART_DEFAULT = 'smart-style-0'
    DARK_ELEGANCE = 'smart-style-1'
    ULTRA_LIGHT = 'smart-style-2'
    GOOGLE_SKIN = 'smart-style-3'
    PIXEL_SMASH = 'smart-style-4'
    GLASS = 'smart-style-5'
    MATERIAL_DESIGN = 'smart-style-6'

    TEMPLATE_STYLE_CHOICES = (
        (SMART_DEFAULT, 'default'),
        (DARK_ELEGANCE, 'dark elegance'),
        (ULTRA_LIGHT, 'ultra light'),
        (GOOGLE_SKIN, 'google skin'),
        (PIXEL_SMASH, 'pixel smash'),
        (GLASS, 'glass'),
        (MATERIAL_DESIGN, 'material design'),
    )
    schema_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    style = models.CharField(
        max_length=14,
        choices=TEMPLATE_STYLE_CHOICES,
        default=SMART_DEFAULT,
    )
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True
