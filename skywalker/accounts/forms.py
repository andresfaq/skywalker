"""
author: Bryan Tabarez
"""

# third-party
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Fieldset, ButtonHolder, Submit, Row,
    HTML, Field)

# django
from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm

# local
from .models import CustomUser, Employee


class MyUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'is_active',
                 'date_of_birth', 'cellphone', 'dni', 'phone')
    

class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=100,
        required=False)
    last_name = forms.CharField(label="Apellidos", max_length=100,
        required=False)
    email = forms.EmailField(required=True)
    is_active = forms.BooleanField(label="Activo", required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
        widget=forms.PasswordInput)

    address = forms.CharField(max_length=100, required=False)
    date_of_birth = forms.DateField(required=False)
    cellphone = forms.IntegerField(required=False)
    dni = forms.IntegerField(required=False)
    phone = forms.IntegerField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'is_active',
                 'date_of_birth', 'cellphone', 'dni', 'phone')

    def __init__(self, *args, **kwargs):
        if kwargs.get("instance", None) is not None:
            if hasattr(kwargs["instance"], "user"):
                kwargs['initial'] = forms.models.model_to_dict(
                                        instance=kwargs["instance"].user)
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset( ('User details'),
                'email',
                'password1',
                'password2',
                'is_active',
            ),
            Fieldset( ('Personal details'),
                'dni',
                'first_name',
                'last_name',
                'address',
                'date_of_birth',
                'cellphone',
                'phone',
            ),
            ButtonHolder(
                HTML('<div class="form-actions">'),
                Submit('Submit', 'Save', css_class='button btn-primary'),
                HTML('</div>'),
            )
        )


class EmployeeForm(MyUserCreationForm, forms.ModelForm):
        
    class Meta:
        model = Employee
        fields = ('employee_type',)

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # Get the 'layout' built in UserCreationForm
        user_layout = self.helper.layout
        layout = Layout(
            Fieldset( ('Employee details'),
                'employee_type'
            ),
            user_layout,
        )
        self.helper.layout = layout
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # El email del usuario que se estA editando
        current_user_email = False
        if hasattr(self.instance, "user"):
            if self.instance.user.email == email:
                current_user_email = True
        if email and get_user_model().objects.filter(email__iexact=email).exists() and not current_user_email:
            raise forms.ValidationError(u'User with this Email already exists!')
        return email

    def save(self):
        """
        NOTA: Antes de guardar el empleado se debe establecer los permisos,
            para esto es necesario estEn definidos los grupos!
        """
        user_form = MyUserCreationForm(self.cleaned_data)
        if hasattr(self.instance, "user"):
            user_form = MyUserChangeForm(self.cleaned_data,
                                         instance=self.instance.user)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            self.instance.user = user
            self.instance.save()
            return self.instance