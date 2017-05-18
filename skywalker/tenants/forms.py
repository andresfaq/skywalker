from django import forms
from .models import Tenant
class TenantForm(forms.ModelForm):
    class Meta:
        SMART_DEFAULT = 'smart-style-0'
        DARK_ELEGANCE = 'smart-style-1'
        ULTRA_LIGHT = 'smart-style-2'
        GOOGLE_SKIN = 'smart-style-3'
        PIXEL_SMASH = 'smart-style-4'
        GLASS = 'smart-style-5'
        MATERIAL_DESIGN = 'smart-style-6'
        BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
        TEMPLATE_STYLE_CHOICES = (
            (SMART_DEFAULT, 'default'),
            (DARK_ELEGANCE, 'dark elegance'),
            (ULTRA_LIGHT, 'ultra light'),
            (GOOGLE_SKIN, 'google skin'),
            (PIXEL_SMASH, 'pixel smash'),
            (GLASS, 'glass'),
            (MATERIAL_DESIGN, 'material design'),
        )

        model = Tenant
        fields = ('schema_name', 'name', 'style', 'paid_until', 'on_trial')
        widgets = {
            'style':forms.Select(choices=TEMPLATE_STYLE_CHOICES),
            'paid_until': forms.TextInput(attrs={'class':"datepicker", 'data-dateformat':'yy-mm-dd'}),
            'on_trial': forms.RadioSelect(choices=[
            (True, 'On Trial'),
            (False, 'On Paid')]),
        }