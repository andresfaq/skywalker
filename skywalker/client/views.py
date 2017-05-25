from django.shortcuts import render

from baseapp.models import Pizza


def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'client/index.html',{'pizzas': pizzas})