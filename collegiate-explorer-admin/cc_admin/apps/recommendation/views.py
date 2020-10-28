from JsonResponseResult import JsonResponseResult
import logging

logger = logging.getLogger('django')
#Done
def index(request):
    """
    this func is using to render the index page when user first click our app.
    :param request: Nothing send here.
    :return: no matter what happened you need to return a dict_list (element in list is dict)
    [{
        'id': '1',                      # -> school_id (str)
        'name': 'University of AAAAAA', # -> school name (str)
        'logo': 'school_logo.jpg',      # -> school-name.jpg (str) e.g. university-of-southern-california.jpg
        'desc': '',                     # -> school description (str)
        'rating': {
            'Niche': 5,                 # -> niche score  (float)
            'CC': 3,                    # -> college confidential score  (float)
        },
        'review': '3453',               # -> # of review (str)
        'detail': 'detail/1',           # -> its detail link, just combine detail + "/" + school_id
        'address': '1420 22nd W St, Los Angeles, CA, 90007',
        'tuition': '$17,234'            # -> tuition (str)
    }, {}, ...]
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    data = [
        {
            'id': '1',
            'name': 'University of AAAAAA',
            'logo': 'school_logo.jpg',
            'desc': 'this is dessc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'A': 5,
                'B': 3,
                'A_val': '5',
                'B_val': '3'
            },
            'review': '3453',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234',
            'school_type': 'Private School',
            'ACT': '1500-1570',
            'acceptance_rate': '7.88%'
        },
        {
            'id': '2',
            'name': 'University of bbbbbbbb',
            'logo': 'school_logo2.jpg',
            'desc': 't is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'A': 2,
                'B': 3,
                'A_val': '2',
                'B_val': '3'
            },
            'review': '3453',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234',
            'school_type': 'Private School',
            'ACT': '1500-1570',
            'acceptance_rate': '7.88%'
        },
        {
            'id': '3',
            'name': 'University of cCCCCC',
            'logo': 'school_logo.jpg',
            'desc': 'this is desc isthis is des desc this isthis is desc this isthis is desc this isthi is desc this is',
            'rating': {
                'A': 4,
                'B': 3,
                'A_val': '4',
                'B_val': '3'
            },
            'review': '3453',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234',
            'school_type': 'Private School',
            'ACT': '1500-1570',
            'acceptance_rate': '7.88%'
        }
    ]
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
