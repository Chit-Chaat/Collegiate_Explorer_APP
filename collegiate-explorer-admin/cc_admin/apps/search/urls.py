__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/19/2020 6:35 PM'

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('query', csrf_exempt(views.index)),
    path('test', views.testNeo4j, name='just_for_test'),
    path('init', views.init_filter_option)
]
