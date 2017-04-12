from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import logout
# Create your views here.

# Bryan: Not used
class DashboardView(TemplateView):
    template_name = "base.html"


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
            if hasattr(user, "client"):
                user_role = "client"
            elif hasattr(user, "employee"):
                user_role = user.employee.employee_type
            request.session["user_role"] = user_role
            return render(request, "base.html")
        else:
            logout(request)
            # return redirect('accounts:login')
            return render(request, "index.html")


index = IndexView.as_view()