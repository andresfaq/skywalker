from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import logout


class IndexView(View):
    """
    Author: Bryan Tabarez
    Render the template if the user is authenticated, and sets the session
    variable 'user_role'
    """
    
    def dispatch(self,request,*args,**kwargs):
        user = request.user
        if user.is_authenticated() and user.is_active and not user.is_staff:
            # Session variable available in all templates
            user_role = ""
            if hasattr(user, "employee"):
                user_role = user.employee.employee_type
            else:
                user_role = "client"
                # redirect to main page of client <-----------------------------
            request.session["user_role"] = user_role
            return redirect('login')

        else:
            logout(request)
            # return redirect('accounts:login')
            return redirect('client:client_index')


index = IndexView.as_view()