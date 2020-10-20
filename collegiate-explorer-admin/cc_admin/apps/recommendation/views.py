from JsonResponseResult import JsonResponseResult


def index(request):
    data = [{
        'id': '1',
        'name': 'University of AAAAAA',
        'logo': 'school_logo.jpg',
        'desc': 'this is desc this is this is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
        'rating': {
            'A': 5,
            'B': 3,
            'A_val': '5',
            'B_val': '3'
        },
        'review': '3453',
        'level': 'A',
        'detail': 'detail/school_id',
        'address': '1420 22nd W St, Los Angeles, CA, 90007',
        'tuition': '$17,234'
    },
        {
            'id': '2',
            'name': 'University of bbbbbbbb',
            'logo': 'school_logo2.jpg',
            'desc': 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'A': 2,
                'B': 3,
                'A_val': '2',
                'B_val': '3'
            },
            'review': '3453',
            'level': 'A',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234'
        },
        {
            'id': '3',
            'name': 'University of cCCCCC',
            'logo': 'school_logo.jpg',
            'desc': 'this is desc this is this is desc this isthis is des desc this isthis is des desc this isthis is des desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'A': 4,
                'B': 3,
                'A_val': '4',
                'B_val': '3'
            },
            'review': '3453',
            'level': 'A',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234'
        }]
    return JsonResponseResult().error(data=data)

"""
normally, u just initialize a JsonResponseResult obj and dot ok(). 
and send back to the data you queried

Api response will be like this:
{
  "code": 200,
  "msg": "OK",
  "data": .... (list, dict, or other thing)
}

statue code is important,


if there is a mistake, no matter caused by user or server, you 
also need to response a proper json, and tell front end, what happened.

about this situation, you can use JsonResponseResult().error(data=data)

{
  "code": 404,
  "msg": "ERROR",
  "data": .... (list, dict, or null)
}

you can also specify the reason why this error happened.
you can use JsonResponseResult().error(msg="balblabla")
or even you can use other status code 
JsonResponseResult().error(code=503, msg="balblabla")

for you reference, the status code meaning can be found from this link:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

"""
