"""
author: Bryan Tabarez
"""

# django
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import (LoginRequiredMixin,
    PermissionRequiredMixin)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import (DeleteView, ListView, UpdateView, CreateView,
    TemplateView)

# local
from .models import Employee, Client
from .forms import EmployeeForm, MyUserCreationForm


class LoginView(TemplateView):
    template_name = "account/login.html"
    
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        user = request.user
        #Si el usuario esta autenticado, se redirecciona al index
        if user.is_authenticated() and not user.is_staff and user.is_active:
            return redirect('index')
        # SI No esta autenticado o esta autenticado como admin
        else:
            logout(request)
            return render(request, self.template_name, context)
            
    def post(self,request,*args,**kwargs):
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                if user.is_staff:
                    # Return an 'invalid login' error message.
                    raise Http404("Usuario Staff!")
                else:
                    # Redirect to a success page.
                    login(request, user)
                    return redirect('index')
            else:
                # Return a 'disabled account' error message
                return redirect('account_inactive')
        else:
            context = self.get_context_data(**kwargs)
            messages.warning(
                request,
                'the email address or password you entered is not valid')
            return render(request, self.template_name, context)


login_view = LoginView.as_view()


class ListUserView(ListView): 
    # permission_required = 'accounts.change_employee'
    model = get_user_model()
    template_name = 'account/user_list.html'


user_list = ListUserView.as_view()


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = MyUserCreationForm
    model = get_user_model()
    template_name = 'object/object_form.html'
    success_message = 'User successfully created!'
    success_url = reverse_lazy('accounts:user_list')

    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['form_title'] = "Create an user"
        return context


user_new = CreateUserView.as_view()


class ListEmployeeView(ListView): 
    # permission_required = 'accounts.change_employee'
    model = Employee
    template_name = 'account/employee_list.html'


employee_list = ListEmployeeView.as_view()


class CreateEmployeeView(SuccessMessageMixin, CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'object/object_form.html'
    success_message = 'Employee successfully created!'
    success_url = reverse_lazy('accounts:employee_list')

    def get_context_data(self, **kwargs):
        context = super(CreateEmployeeView, self).get_context_data(**kwargs)
        context['form_title'] = "Create an employee"
        return context


employee_new = CreateEmployeeView.as_view()


class UpdateEmployeeView(SuccessMessageMixin, UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'object/object_form.html'
    success_message = 'Employee successfully updated!'
    success_url = reverse_lazy('accounts:employee_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateEmployeeView, self).get_context_data(**kwargs)
        context['form_title'] = "Update an employee"
        return context


employee_edit = UpdateEmployeeView.as_view()