__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/19/2020 6:35 PM'

from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.detail_list, name='detail_list'),
]
