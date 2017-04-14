from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, ButtonHolder, Submit, Row,
    HTML, Field)
from django import forms
from baseapp.models import Ingredient

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'description', 'price')

    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'price',
            ButtonHolder(
                HTML('<div class="form-actions">'),
                Submit('Submit', 'Save', css_class='button btn-primary'),
                HTML('</div>'),
            )
        )