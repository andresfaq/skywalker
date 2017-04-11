from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name = "account/login.html"
    
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        user = request.user
        #Si el usuario esta autenticado, se direcciona al index
        if user.is_authenticated() and not user.is_staff and user.is_active:
            return redirect('index')
        # SI No esta autenticado o esta autenticado como admin
        else:
            logout(request)
            return render(request, self.template_name, context)
            
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
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
                return redirect('cuenta-inactiva')
        else:
            context = self.get_context_data(**kwargs)
            messages.warning(
                request,
                'El usuario y/o la contraseña que especificaste no son correctos.')
            return render(request, self.template_name, context)


login = LoginView.as_view()