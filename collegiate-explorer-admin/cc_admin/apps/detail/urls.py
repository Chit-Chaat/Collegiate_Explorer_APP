__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/19/2020 6:35 PM'

from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.get_basic_info),
    path('popular_major/<str:id>', views.get_popular_major),
    path('ranking/history/<str:id>', views.get_ranking_data)
]
