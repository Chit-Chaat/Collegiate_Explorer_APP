import json

from JsonResponseResult import JsonResponseResult
from Neo4jConnectionPool import ConnectionPool
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
    this func only accept post request, which mean all the params wont show in the path (url)

    :param request: all params saved here. there are:
        content: the value in the input box
        school_type: public | private | other
        filter_content: this is an obj
            if user did not use the filter, you will get a "{}"
            or you will receive an obj like this
            {
                'area': 'New England',
                'major': 'Music, theatre, or dance',
                'tuition': '>= $5k',
                'act': [28, 32],
                'sat': [1500, 1600]
            }
            you can convert it into dict and do further process.
    :return:
    """
    if request.method == "POST" and request.POST:
        school_type = request.POST.get('school_type')
        input_content = request.POST.get('content')
        filter_content = request.POST.get('filter_content')
        print("school_type -> ", school_type)
        print("input_content -> ", input_content)
        print("filter_content -> ", filter_content)
        if "{}" == filter_content:
            # user did not use filter
            print("filert is null")
        else:
            # user used filter
            selected_tags = json.loads(filter_content)
            print(selected_tags['area'])
    return JsonResponseResult().ok(data="asdasdas")


def init_filter_option(request):
    """
    this func return some data to render the filter when the page first load.

    :param request:
    :return:
    """
    data = {
        "areas": [
            'New England', 'Mid East', 'Great Lakes',
            'Plains', 'Southeast', 'Southwest',
            'Rocky Mountains', 'Far West', 'Outlying areas'],
        "marjors": [
            'Humanities',
            'Natural sciences or mathematics',
            'Social sciences ',
            'Architecture or urban planning',
            'Art and design',
            'Business',
            'Dentistry',
            'Education',
            'Engineering',
            'Law',
            'Medicine',
            'Music, theatre, or dance',
            'Nursing',
            'Pharmacy',
            'Public health',
            'Public policy',
            'Social work',
            'Other'],
        "tuitions": ['>= $5k', '>= $10k', '>= $15k']
    }
    return JsonResponseResult().ok(data=data)


def search_by_tag(request, tag="tag_str"):
    """
     user clicked tag label.
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
         'tuition': '$17,234',           # -> tuition (str)
         'school_type': 'Private School',# -> school type
         'ACT': '1500-1570',             # -> ACT score range
         'acceptance_rate': '7.88%'
     }, {}, ...]
     and use JsonResponseResult().ok(data=data) return
     if there is any exception raised,
     use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
     """
    logger.info("revoked func search/views.py 'search_by_tag' func. tag -> " + tag)
    data = [
        {
            'id': '6',
            'name': 'University of DDDDDD',
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
            'id': '7',
            'name': 'University of EEEEE',
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
            'id': '9',
            'name': 'University of FFFFF',
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
    return JsonResponseResult().ok(data=data)

def testNeo4j(request):
    """
    This func just tell you how to connect to neo4j and do the search
    :param request:
    :return:
    """
    connection = ConnectionPool()
    # result = connection.executeQuery(
    #     "MATCH (cloudAtlas2 {title: $param, tagline: $param1}) RETURN cloudAtlas2",
    #         param="Cloud Atlas",
    #         param1="Everything is connected")
    result2 = connection.executeQuery(
        "MATCH (tom:Person {name: \"Tom Hanks\"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies")
    return JsonResponseResult().ok(data=result2)
    # http://127.0.0.1:8000/search/test
