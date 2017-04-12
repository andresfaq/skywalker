from django.conf.urls import url, include
from . import views

urlpatterns = [
    
    url(r'^login/$', views.login, name='login'),

    # Users
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^user/new/', views.user_new, name='user_new'),

    # Employees
    url(r'^employees/$', views.employee_list, name='employee_list'),
    url(r'^employee/new/', views.employee_new, name='employee_new'),
    url(r'^employee/(?P<pk>[0-9]+)/edit/', views.employee_edit,
        name='employee_edit'),

    # Clients

]