__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/19/2020 6:35 PM'

from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.get_basic_info),
    path('popular_major/<str:id>', views.get_popular_major),
    path('location/<str:id>', views.get_loc_data),
    path('score/<str:id>', views.get_score_data),
    path('similar/<str:id>', views.get_similar_school_data),
    path('fame/<str:id>', views.get_fame_property),
    path('subjective/<str:id>', views.get_subject_info_data),
    path('sentimental/<str:id>', views.get_sentimental_tags),
]
