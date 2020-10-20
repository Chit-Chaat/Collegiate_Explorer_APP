import json

from django.http import HttpResponse

# from .ResponseResult import ResponseResult


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
    return HttpResponse(data)

# @api_view(['GET'])
# def task_detail(request, pk):
#     data = [{'id': str(pk),
#              'name': "1",
#              'gender': "1"},
#             {'id': "2",
#              'name': "2",
#              'gender': "2"},
#             {'id': "3",
#              'name': "3",
#              'gender': "3"}]
#     return ResponseResult(data=json.dumps(data),
#                           code=200, msg="success",
#                           status=status.HTTP_200_OK)
