
from django.http import HttpResponse

from JsonResponseResult import JsonResponseResult


def index(request):
    return HttpResponse("Hello, world. You're at the detail index.")


def detail_list(request):
    data = [{'id': "1",
             'name': "1",
             'gender': "1"},
            {'id': "2",
             'name': "2",
             'gender': "2"},
            {'id': "3",
             'name': "3",
             'gender': "3"}]
    return JsonResponseResult(code=404, data=data, msg="OK")


def get_param(request, year=2005):
    data = [{'id': "1",
             'name': "1",
             'gender': "1"},
            {'id': "2",
             'name': "2",
             'gender': "2"},
            {'id': "3",
             'name': "3",
             'gender': "3"}, {
                'year': str(year)
            }]
    return JsonResponseResult(code=200, data=data, msg="OK")
