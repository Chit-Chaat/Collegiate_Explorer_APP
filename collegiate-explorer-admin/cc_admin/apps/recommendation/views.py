from JsonResponseResult import JsonResponseResult
import logging

logger = logging.getLogger('django')

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

"""
there are two way to do query(since this project mainly need us to do query not much update)
the first way is to use $param, to change your query dynamically.
    if you need to use more read about ./tests.py
    result = connection.executeQuery(
        "MATCH (cloudAtlas2 {title: $param}) RETURN cloudAtlas2", param="Cloud Atlas")

another way to do query is just prefix all your condition
    result2 = connection.executeQuery(
        "MATCH (cloudAtlas {title: \"Cloud Atlas\"}) RETURN cloudAtlas")

"""


def index(request):
    """
    this func is using to render the index page when user first clicked our app.
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
    logger.info("revoked func 'index'")
    data = [
        {
            'id': '1',
            'name': 'University of AAAAAA',
            'logo': 'school_logo.jpg',
            'desc': 'this is dessc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'Niche': 5,
                'CC': 3
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
                'Niche': 2,
                'CC': 3
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
                'Niche': 4,
                'CC': 3
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


def get_recommend_tags(request):
    """

    :param request:
    :param id: you will receive a school id (str) (required)
    :return: you need to return a list of recommend tag, enabling people do quick search.
    [{
        'name': 'USC',
        'type': 'primary',  # primary | success | info | warning | danger
        'link': ''},

    },{},...]
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    logger.info("revoked func 'get_recommend_tags'")
    data = [
        {'name': 'USC', 'type': 'primary', 'link': ''},
        {'name': 'Best CS in LA', 'type': 'success', 'link': ''},
        {'name': 'xxxxxxxxxxx', 'type': 'info', 'link': ''},
        {'name': 'Top 10 DS programs', 'type': 'warning', 'link': ''},
        {'name': '#Don\'t go there', 'type': 'danger', 'link': ''}
    ]
    return JsonResponseResult().ok(data=data)
