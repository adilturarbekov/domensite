from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.host_list, name = 'host_list')

]