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
        'tuition': '$17,234',           # -> tuition (str)
        'school_type': 'Private School',# -> school type
        'ACT': '1500-1570',             # -> ACT score range
        'acceptance_rate': '7.88%'
    }, {}, ...]
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    logger.info("revoked func 'index'")
    connection = ConnectionPool()
    result = connection.executeQuery(
        "\
        match (node_school)-[r:HAS_QS_RANK]->(node_qs_rank)\
        where 1 <=toInteger(node_qs_rank.name) <= 15\
        match (node_school)-[:AVG_ACT]->(node_avg_act)\
        match (node_school)-[:HAS_SAT_MAX_OF]->(node_sat_max)\
        where node_sat_max.name is not null\
        match (node_school)-[:HAS_SAT_MIN_OF]->(node_sat_min)\
        where node_sat_min.name is not null\
        match (node_school)-[:HAS_TUITION_OF]->(node_tuition)\
        match (node_school)-[:ID]->(node_id)\
        match (node_school)-[:HAS_LOGO]->(node_logo)\
        match (node_school)-[:HAS_WEBSITE]->(node_web)\
        match (node_school)-[:HAS_CC_SCORE]->(node_cc_score)\
        match (node_school)-[:HAS_ADDRESS]->(node_address)\
        match (node_school)-[:HAS_STATE]->(node_state)\
        match (node_school)-[:HAS_CITY]->(node_city)\
        match (node_school)-[:HAS_ZIP]->(node_zip)\
        match (node_school)-[:HAS_TUITION_OF]->(node_tuition)\
        match (node_school)-[:IS_TYPE]->(node_type)\
        match (node_school)-[:ACCEPT_RATE]->(node_accept_rate)\
        match (node_school)-[:HAS_TELEPHONE]->(node_telephone)\
        match (node_school)-[:AVG_GPA]->(node_gpa)\
        return node_id.name, node_school.name, node_logo.name,\
        node_cc_score.name, node_address.name, node_state.name,\
        node_city.name, node_zip.name, node_tuition.name,\
        node_type.name, node_accept_rate.name, node_sat_max.name,\
        node_sat_min.name, node_telephone.name, node_avg_act.name,\
        node_qs_rank.name, node_gpa.name, node_web.name\
        order by toInteger(node_qs_rank.name)\
        limit 24\
        ")

    data = []
    for school in result:
        cc_score = float(school['node_cc_score.name'])
        cc_min = 0
        cc_max = 400
        cc_rating = 0
        for i in range(5):
            if cc_min <= cc_score <= cc_max:
                cc_rating = i
            else:
                cc_min = cc_max
                cc_max += 500 
        obj =  {
            'id': school['node_id.name'],
            'name': school['node_school.name'],
            'logo': 'school_logo.jpg',
            'desc': 'desc',
            'rating': {
                'Niche': 4,
                'CC': cc_rating
            },
            'detail': 'detail/' + school['node_id.name'],
            'address': school['node_address.name'] + ' ' +
                       school['node_city.name'] + ', ' +
                       school['node_state.name'] + ' ' +
                       school['node_zip.name'],
            'tuition': '$' + str(int(float(school['node_tuition.name']))),
            'school_type': school['node_type.name'].capitalize(),
            'ACT': school['node_sat_min.name'] + '-' + school['node_sat_max.name'],
            'acceptance_rate': str(round(float(school['node_accept_rate.name'])*100, 2)) + '%',
            'link': school['node_web.name']
        }
        data.append(obj)
    return JsonResponseResult().ok(data=data)


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
