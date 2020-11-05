import json
import re

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

            #TODO -> niche
            when you use niche filter
            you will receive this obj
            {
                "academic":4,
                "dorms":3,
                "food":2,
                "location":1,
                "safety":0,
                "value":1
            }
            [0-4], all value will be int number
            4 -> A+, A, A-,
            3 -> B+, B, B-,
            2 -> C+, C, C-,
            1 -> D+, D, D-,
            0 -> NG

    :return:
    """
    if request.method == "POST" and request.POST:
        search_type = request.POST.get('search_type')
        input_content = request.POST.get('content')
        filter_content = request.POST.get('filter_content')
        print("search_type -> ", search_type)
        print("input_content -> ", input_content)
        print("filter_content -> ", filter_content)
        if "{}" == filter_content:
            # user did not use filter
            print("filert is null")
        else:
            # user used filter
            selected_tags = json.loads(filter_content)

    filter_content = eval(filter_content)
    connection = ConnectionPool()

    if input_content != '':
        uni = []
        for item in input_content.split():
            print(item)
            if len(item) > 3:
                uni.append(item.capitalize())
            else:
                uni.append(item)

        uni = ' '.join(uni)
        result = connection.executeQuery("\
            match (node_school {name: '" + uni + "'})\
            match (node_school)-[:AVG_ACT]->(node_avg_act) \
            match (node_school)-[:HAS_TUITION_OF]->(node_tuition)\
            match (node_school)-[:HAS_SAT_MAX_OF]->(node_sat_max)\
            match (node_school)-[:HAS_SAT_MIN_OF]->(node_sat_min)\
            match (node_school)-[r:HAS_QS_RANK]->(node_qs_rank)\
            match (node_school)-[:ID]->(node_id)\
            match (node_school)-[:HAS_LOGO]->(node_logo)\
            match (node_school)-[:HAS_CC_SCORE]->(node_cc_score)\
            match (node_school)-[:HAS_ADDRESS]->(node_address)\
            match (node_school)-[:HAS_STATE]->(node_state)\
            match (node_school)-[:HAS_CITY]->(node_city)\
            match (node_school)-[:HAS_ZIP]->(node_zip)\
            match (node_school)-[:HAS_WEBSITE]->(node_web)\
            match (node_school)-[:IS_TYPE]->(node_type)\
            match (node_school)-[:ACCEPT_RATE]->(node_accept_rate)\
            match (node_school)-[:HAS_TELEPHONE]->(node_telephone)\
            match (node_school)-[:HAS_STUDENT_FACULTY_RATIO_OF]->(node_s_f_ratio)\
            match (node_school)-[:HAS_SETTING]->(node_school_setting)\
            match (node_school)-[:HAS_SIZE]->(node_size)\
            return node_id.name, node_school.name, node_logo.name,\
            node_cc_score.name, node_address.name, node_state.name,\
            node_city.name, node_zip.name, node_tuition.name, node_web.name,\
            node_type.name, node_accept_rate.name, node_sat_max.name,\
            node_sat_min.name, node_telephone.name,  node_qs_rank.name,\
            node_s_f_ratio.name,node_school_setting.name, node_size.name,\
            node_avg_act.name LIMIT 90\
        ")
        data = []
        for school in result:
            if school['node_accept_rate.name'] != 'N/A':
                school['node_accept_rate.name'] = str(round(float(school['node_accept_rate.name']) * 100, 2)) + '%'

            obj = {
                'id': school['node_id.name'],
                'name': school['node_school.name'],
                'logo': extract_logo_name(school['node_logo.name']),
                'desc': school['node_school.name'] + " is a " + school.get('node_type.name', 'private')
                        + " research university in " + school.get('node_city.name', 'somewhere')
                        + ". And its campus located in " + school.get('node_school_setting.name', 'unknown') + " area. "
                        + "And its campus size is " + school.get('node_size.name', 'unknown') + ". "
                        + "And its student-faculty-ratio is " + school.get('node_s_f_ratio.name', 'unknown') + " . ",
                'rating': {
                    'QS': format_qs_score(school.get('node_qs_rank.name', '')),
                    'CC': min(int(float(school['node_cc_score.name']) / 400) + 1, 5)
                },
                'detail': 'detail/' + school.get('node_id.name', ''),
                'address': school.get('node_address.name', '') + ' ' +
                           school.get('node_city.name', '') + ' ' +
                           school.get('node_state.name', '') + ', ' +
                           school.get('node_zip.name', ''),
                'tuition': '$' + school.get('node_tuition.name', ''),
                'school_type': school.get('node_type.name', '').capitalize(),
                'ACT': school.get('node_sat_min.name', '') + '-' +
                       school.get('node_sat_max.name', ''),
                'acceptance_rate': school.get('node_accept_rate.name', ''),
                'link': school.get('node_web.name', '')
            }
            data.append(obj)

        return JsonResponseResult().ok(data=data)

    majors = area = act = s_type = sat_max = sat_min = tuition = ""
    if 'major' in filter_content:
        major = filter_content['major'].split(',')
        if len(major[0]) != 0:
            for item in major:
                majors += "match (node_school)-[:HAS_N_POPULAR_MAJORS]->(node_popular_major {name: '" + str(
                    item) + "'})         "
        else:
            majors = " "

    if search_type != '':
        s_type = "match (node_school)-[:IS_TYPE]->(node_school_type {name:'" + search_type + "'})"

    for key, value in filter_content.items():
        if key == 'area' and value != '':
            area = "match (node_school)-[:IN_REGION]->(node_region {name: '" + value + "'})" + " "
        if key == 'act' and value != '':
            act = "where " + str(filter_content['act'][0]) + " <= toInteger(node_avg_act.name) <= " + str(
                filter_content['act'][1]) + " "
        if key == 'sat' and value != '':
            sat_max = "where " + str(filter_content['sat'][0]) + "<= toInteger(node_sat_max.name) <= " + str(
                filter_content['sat'][1]) + " "
            sat_min = "where " + str(filter_content['sat'][0]) + " <= toInteger(node_sat_min.name)<= " + str(
                filter_content['sat'][1]) + " "

        if key == 'tuition' and value != '':
            tuition = "where toInteger(node_tuition.name) <= " + str(
                int(''.join([i for i in filter_content['tuition'] if i.isdigit()])) * 1000) + " "

    result = connection.executeQuery(
        area + \
        s_type + "\
         match (node_school)-[:AVG_ACT]->(node_avg_act) " \
        + act + "\
         match (node_school)-[:HAS_TUITION_OF]->(node_tuition) " + \
        tuition + majors + "\
         match (node_school)-[:HAS_SAT_MAX_OF]->(node_sat_max) " + \
        sat_max + "\
         match (node_school)-[:HAS_SAT_MIN_OF]->(node_sat_min) " + \
        sat_min + "\
         match (node_school)-[r:HAS_QS_RANK]->(node_qs_rank)\
         match (node_school)-[:ID]->(node_id)\
         match (node_school)-[:HAS_LOGO]->(node_logo)\
         match (node_school)-[:HAS_CC_SCORE]->(node_cc_score)\
         match (node_school)-[:HAS_ADDRESS]->(node_address)\
         match (node_school)-[:HAS_STATE]->(node_state)\
         match (node_school)-[:HAS_CITY]->(node_city)\
         match (node_school)-[:HAS_ZIP]->(node_zip)\
         match (node_school)-[:HAS_WEBSITE]->(node_web)\
         match (node_school)-[:IS_TYPE]->(node_type)\
         match (node_school)-[:ACCEPT_RATE]->(node_accept_rate)\
         match (node_school)-[:HAS_TELEPHONE]->(node_telephone)\
         match (node_school)-[:HAS_STUDENT_FACULTY_RATIO_OF]->(node_s_f_ratio)\
         match (node_school)-[:HAS_SETTING]->(node_school_setting)\
         match (node_school)-[:HAS_SIZE]->(node_size)\
         return node_id.name, node_school.name, node_logo.name,\
         node_cc_score.name, node_address.name, node_state.name,\
         node_city.name, node_zip.name, node_tuition.name, node_web.name,\
         node_type.name, node_accept_rate.name, node_sat_max.name,\
         node_sat_min.name, node_telephone.name,  node_qs_rank.name,\
         node_s_f_ratio.name,node_school_setting.name, node_size.name,\
         node_avg_act.name LIMIT 90\
         ")

    data = []
    for school in result:
        if school['node_accept_rate.name'] != 'N/A':
            school['node_accept_rate.name'] = str(round(float(school['node_accept_rate.name']) * 100, 2)) + '%'

        obj = {
            'id': school['node_id.name'],
            'name': school['node_school.name'],
            'logo': extract_logo_name(school['node_logo.name']),
            'desc': school['node_school.name'] + " is a " + school.get('node_type.name', 'private')
                    + " research university in " + school.get('node_city.name', 'somewhere')
                    + ". And its campus located in " + school.get('node_school_setting.name', 'unknown') + " area. "
                    + "And its campus size is " + school.get('node_size.name', 'unknown') + ". "
                    + "And its student-faculty-ratio is " + school.get('node_s_f_ratio.name', 'unknown') + " . ",
            'rating': {
                'QS': format_qs_score(school.get('node_qs_rank.name', '')),
                'CC': min(int(float(school['node_cc_score.name']) / 400) + 1, 5)
            },
            'detail': 'detail/' + school.get('node_id.name', ''),
            'address': school.get('node_address.name', '') + ' ' +
                       school.get('node_city.name', '') + ' ' +
                       school.get('node_state.name', '') + ', ' +
                       school.get('node_zip.name', ''),
            'tuition': '$' + school.get('node_tuition.name', ''),
            'school_type': school.get('node_type.name', '').capitalize(),
            'ACT': school.get('node_sat_min.name', '') + '-' +
                   school.get('node_sat_max.name', ''),
            'acceptance_rate': school.get('node_accept_rate.name', ''),
            'link': school.get('node_web.name', '')
        }
        data.append(obj)

    return JsonResponseResult().ok(data=data)


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
            'Liberal Arts and Humanities',
            'Kinesiology and Exercise',
            'Business',
            'Psychology',
            'Marketing',
            'Nursing',
            'Sport and Fitness',
            'Agriculture',
            'Managerial',
            'Biology',
            'International Business',
            'Healthcare',
            'Social Science',
            'Public Health',
            'Mathematics',
            'Creative',
            'Criminal Justice and Safety',
            'Radiation',
            'Painting',
            'Photography',
            'Design and Visual',
            'Biblical Studies',
            'Finance',
            'International',
            'Accounting',
            'Economics',
            'Computer Science',
            'English',
            'Electrical Engineering',
            'Mechanical Engineering',
            'Chemical Engineering',
            'Aerospace Engineering',
            'Environmental Engineering',
            'Criminal Justice and Safety Studies',
            'Human Services',
            'Sociology'],
        "tuitions": ['>= $5k', '>= $10k', '>= $15k']
    }

    return JsonResponseResult().ok(data=data)

def tag_query(tag_str):
    connection = ConnectionPool()
    data_objs = []
    for school in tag_str:
        result = connection.executeQuery(
            "match (node_school {name: '" + school + "'})\
            match (node_school)-[:AVG_ACT]->(node_avg_act) \
            match (node_school)-[r:HAS_QS_RANK]->(node_qs_rank) \
            match (node_school)-[:HAS_TUITION_OF]->(node_tuition)\
            match (node_school)-[:HAS_SAT_MAX_OF]->(node_sat_max)\
            match (node_school)-[:HAS_SAT_MIN_OF]->(node_sat_min)\
            match (node_school)-[:ID]->(node_id)\
            match (node_school)-[:IS_TYPE]->(node_school_type)\
            match (node_school)-[:IN_REGION]->(node_region)\
            match (node_school)-[:HAS_LOGO]->(node_logo)\
            match (node_school)-[:HAS_CC_SCORE]->(node_cc_score)\
            match (node_school)-[:HAS_ADDRESS]->(node_address)\
            match (node_school)-[:HAS_STATE]->(node_state)\
            match (node_school)-[:HAS_CITY]->(node_city)\
            match (node_school)-[:HAS_ZIP]->(node_zip)\
            match (node_school)-[:HAS_WEBSITE]->(node_web)\
            match (node_school)-[:IS_TYPE]->(node_type)\
            match (node_school)-[:ACCEPT_RATE]->(node_accept_rate)\
            match (node_school)-[:HAS_STUDENT_FACULTY_RATIO_OF]->(node_s_f_ratio)\
            match (node_school)-[:HAS_SETTING]->(node_school_setting)\
            match (node_school)-[:HAS_SIZE]->(node_size)\
            match (node_school)-[:HAS_TELEPHONE]->(node_telephone)\
            return node_id.name, node_school.name, node_logo.name,\
            node_cc_score.name, node_address.name, node_state.name,\
            node_city.name, node_zip.name, node_tuition.name, node_web.name,\
            node_type.name, node_accept_rate.name, node_sat_max.name,\
            node_sat_min.name, node_telephone.name, node_qs_rank.name, \
            node_s_f_ratio.name,node_school_setting.name, node_size.name,\
            node_avg_act.name LIMIT 90\
        ")
        data_objs.append(result)
    return data_objs
   


def search_by_tag(request, tag="tag_str"):
    """
     user clicked tag label.
     :param tag:
     :param request: Nothing send here.
     :return: no matter what happened you need to return a dict_list (element in list is dict)
     [{
         'id': '1',                      # -> school_id (str)
         'name': 'University of AAAAAA', # -> school name (str)
         'logo': 'school_logo.jpg',      # -> school-name.jpg (str) e.g. university-of-southern-california.jpg
         'desc': '',                     # -> school description (str)
         'rating': {
             'QS': 5,                 # -> niche score  (float)
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

    ivy_league = ['Brown University', 'Columbia University', 'Cornell University', 'Darthmouth College',\
                  'Harvard University', 'University of Pennsylvania', 'Princeton University', 'Yale University']
    uc = ['University of California, Berkeley',  'University of California, Davis','University of California, Santa Cruz',\
          'University of California, Santa Barbara','University of California, San Diego','University of California, Los Angeles',\
          'University of California, Irvine','University of California, Merced', 'University of California, Riverside']
    csu = ['California State University, Bakersfield',  'California State University, Fullerton','California State University, Northridge',\
           'California State University, Long Beach','California State Polytechnic University, Ponoma',\
           'California State University Channel Islands','California State University, Chico','California State University, Dominguez Hills',\
           'California State University, East Bay','California State University, Fresno','California State University, Los Angeles',\
           'California State University Maritime Academy','California State University, Monterey Bay',\
           'California State University, San Bernardino','California State University, San Marcos','California State University, Stanislaus']

    data_objs = []
    if tag == 'Ivy League':
        data_objs = tag_query(ivy_league)
    if tag == 'University of California':
        data_objs = tag_query(uc)
    if tag == 'California State University':
        data_objs = tag_query(csu)

    data = []
    for result in data_objs:
        for school in result:
            if school['node_accept_rate.name'] != 'N/A':
                school['node_accept_rate.name'] = str(round(float(school['node_accept_rate.name']) * 100, 2)) + '%'
 
            obj = {
                'id': school['node_id.name'],
                'name': school['node_school.name'],
                'logo': extract_logo_name(school['node_logo.name']),
                'desc': school['node_school.name'] + " is a " + school.get('node_type.name', 'private')
                        + " research university in " + school.get('node_city.name', 'somewhere')
                        + ". And its campus located in " + school.get('node_school_setting.name', 'unknown') + " area. "
                        + "And its campus size is " + school.get('node_size.name', 'unknown') + ". "
                        + "And its student-faculty-ratio is " + school.get('node_s_f_ratio.name', 'unknown') + " . ",
                'rating': {
                    'QS': format_qs_score(school.get('node_qs_rank.name', '')),
                    'CC': min(int(float(school['node_cc_score.name']) / 400) + 1, 5)
                },
                'detail': 'detail/' + school['node_id.name'],
                'address': school['node_address.name'] + ' ' +
                           school['node_city.name'] + ' ' +
                           school['node_state.name'] + ', ' +
                           school['node_zip.name'],
                'tuition': '$' + school['node_tuition.name'],
                'school_type': school['node_type.name'].capitalize(),
                'ACT': school['node_sat_min.name'] + '-' +
                       school['node_sat_max.name'],
                'acceptance_rate': school['node_accept_rate.name'],
                'link': school['node_web.name']
            }
            data.append(obj)
    '''
    data = [
        {
            'id': '6',
            'name': 'University of DDDDDD2',
            'logo': 'school_logo.jpg',
            'desc': 'this is dessc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'QS': 5,
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
                'QS': 2,
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
                'QS': 4,
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
    '''
    return JsonResponseResult().ok(data=data)


def search_by_major(request, major="major_str"):
    """
     user clicked major label.
     :param major: a str
     :param request: Nothing send here.
     :return: no matter what happened you need to return a dict_list (element in list is dict)
     [{
         'id': '1',                      # -> school_id (str)
         'name': 'University of AAAAAA', # -> school name (str)
         'logo': 'school_logo.jpg',      # -> school-name.jpg (str) e.g. university-of-southern-california.jpg
         'desc': '',                     # -> school description (str)
         'rating': {
             'QS': 5,                 # -> niche score  (float)
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
    logger.info("revoked func search/views.py 'search_by_major' func. major -> " + major)

    connection = ConnectionPool()
    majors = "match (node_school)-[:HAS_N_POPULAR_MAJORS]->(node_popular_major {name: '" + major + "'})         "

    result = connection.executeQuery(
        "match (node_school)-[:AVG_ACT]->(node_avg_act) \
        " + majors + "\
         match (node_school)-[r:HAS_QS_RANK]->(node_qs_rank) \
         match (node_school)-[:HAS_TUITION_OF]->(node_tuition)\
         match (node_school)-[:HAS_SAT_MAX_OF]->(node_sat_max)\
         match (node_school)-[:HAS_SAT_MIN_OF]->(node_sat_min)\
         match (node_school)-[:ID]->(node_id)\
         match (node_school)-[:IS_TYPE]->(node_school_type)\
         match (node_school)-[:IN_REGION]->(node_region)\
         match (node_school)-[:HAS_LOGO]->(node_logo)\
         match (node_school)-[:HAS_CC_SCORE]->(node_cc_score)\
         match (node_school)-[:HAS_ADDRESS]->(node_address)\
         match (node_school)-[:HAS_STATE]->(node_state)\
         match (node_school)-[:HAS_CITY]->(node_city)\
         match (node_school)-[:HAS_ZIP]->(node_zip)\
         match (node_school)-[:HAS_WEBSITE]->(node_web)\
         match (node_school)-[:IS_TYPE]->(node_type)\
         match (node_school)-[:ACCEPT_RATE]->(node_accept_rate)\
         match (node_school)-[:HAS_STUDENT_FACULTY_RATIO_OF]->(node_s_f_ratio)\
         match (node_school)-[:HAS_SETTING]->(node_school_setting)\
         match (node_school)-[:HAS_SIZE]->(node_size)\
         match (node_school)-[:HAS_TELEPHONE]->(node_telephone)\
         return node_id.name, node_school.name, node_logo.name,\
         node_cc_score.name, node_address.name, node_state.name,\
         node_city.name, node_zip.name, node_tuition.name, node_web.name,\
         node_type.name, node_accept_rate.name, node_sat_max.name,\
         node_sat_min.name, node_telephone.name, node_qs_rank.name, \
         node_s_f_ratio.name,node_school_setting.name, node_size.name,\
         node_avg_act.name LIMIT 90\
         ")

    data = []
    for school in result:
        if school['node_accept_rate.name'] != 'N/A':
            school['node_accept_rate.name'] = str(round(float(school['node_accept_rate.name']) * 100, 2)) + '%'

        obj = {
            'id': school['node_id.name'],
            'name': school['node_school.name'],
            'logo': extract_logo_name(school['node_logo.name']),
            'desc': school['node_school.name'] + " is a " + school.get('node_type.name', 'private')
                    + " research university in " + school.get('node_city.name', 'somewhere')
                    + ". And its campus located in " + school.get('node_school_setting.name', 'unknown') + " area. "
                    + "And its campus size is " + school.get('node_size.name', 'unknown') + ". "
                    + "And its student-faculty-ratio is " + school.get('node_s_f_ratio.name', 'unknown') + " . ",
            'rating': {
                'QS': format_qs_score(school.get('node_qs_rank.name', '')),
                'CC': min(int(float(school['node_cc_score.name']) / 400) + 1, 5)
            },
            'detail': 'detail/' + school['node_id.name'],
            'address': school['node_address.name'] + ' ' +
                       school['node_city.name'] + ' ' +
                       school['node_state.name'] + ', ' +
                       school['node_zip.name'],
            'tuition': '$' + school['node_tuition.name'],
            'school_type': school['node_type.name'].capitalize(),
            'ACT': school['node_sat_min.name'] + '-' +
                   school['node_sat_max.name'],
            'acceptance_rate': school['node_accept_rate.name'],
            'link': school['node_web.name']
        }
        data.append(obj)

    return JsonResponseResult().ok(data=data)


def extract_logo_name(logo_url):
    if logo_url and logo_url != 'N/A':
        return logo_url.split('/')[-1].split('_')[0] + ".jpg"
    return "default.png"


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


def format_qs_score(score_str):
    """
    help you generate a qs score
    1 - 100 : 5
    141-200 : 4
    =100: 4
    N/A 3
    :param score_str:
    :return:
    """
    score = 3
    if not score_str or score_str != "N/A":
        try:
            parts = int(list(filter(lambda val: val,
                                    list(re.split('-|=', score_str))))[0])
        except:
            return 3
        score = 5 - int(parts / 100)
        if score > 5 or score < 1:
            return 3
    return score
