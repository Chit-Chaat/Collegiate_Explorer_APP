import json
import logging
import os

from JsonResponseResult import JsonResponseResult
from Neo4jConnectionPool import ConnectionPool

logger = logging.getLogger('django')
review_tags = None
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


def get_basic_info(request, id='2005'):
    """
    this fun will be revoked when user click the detail page
    :param request:
    :param id: you will receive a school id (str) (required)
    :return: you need to return an obj of basic info of this school
    {
        "title_info": {
            'main_title': "",
            'duration': "",
            'school_type': "",
            'location': "",
            'school_link': ""
        },
         "desc_info": {
            'title': "",
            'location': "",
            'avg_score': {
                'reading': "",
                'math': "",
                'composite': ""
            },
            'expected_salary': "",
            'cost': {
                'net_price': "",
                'national': "",
                'financial_aid': "",
                'avg_aid_award': ""
            },
            'admission': {
                'acceptance_rate': "",
                'application_ddl': ""
            },
            'students': {
                'undergraduate': "",
                'graduate': "",
                'international': ""
            }
         }
    }
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    logger.info("func 'get_basic_info' get a param id -> " + id)
    connection = ConnectionPool()
    result = connection.executeQuery(
        "\
        match(n)-[]-(m {name: '" + id + "'})\
        return n.name\
        "
    )
    name = result[0]['n.name']
    result = connection.executeQuery(
        "\
        match(n)-[]-(m {name: '" + id + "'})\
        match(n)-[]-(c)\
        return labels(c) as c, c.name\
        "
    )
    detail = {}
    for item in result:
        if item['c'][0] == "school_type_node":
            detail['setting'] = item['c.name'].capitalize()
        if item['c'][0] == "web_node":
            detail['website'] = item['c.name']
        if item['c'][0] == "read_sat_node":
            detail['read_sat'] = item['c.name']
        if item['c'][0] == "math_sat_node":
            detail['math_sat'] = item['c.name']
        if item['c'][0] == "act_node":
            detail['act'] = item['c.name']
        if item['c'][0] == "addr_node":
            detail['address'] = item['c.name']
        if item['c'][0] == "city_node":
            detail['city'] = item['c.name']
        if item['c'][0] == "state_node":
            detail['state'] = item['c.name']
        if item['c'][0] == "zip_node":
            detail['zip'] = item['c.name']
        if item['c'][0] == "med_earn_6_years_node":
            detail['med_earn'] = item['c.name']
        if item['c'][0] == "tuition_node":
            detail['tuition'] = item['c.name']
        if item['c'][0] == "average_aid_node":
            detail['avg_aid'] = item['c.name']
        if item['c'][0] == "accept_rate_node":
            if item['c.name'] != 'N/A':
                detail['accept_rate'] = str(int(float(item['c.name']) * 100)) + '%'
            else:
                detail['accept_rate'] = item['c.name']
        if item['c'][0] == "app_dead_node":
            detail['app_dead'] = item['c.name']
        if item['c'][0] == "app_fee_node":
            detail['app_fee'] = item['c.name']
        if item['c'][0] == "undergrad_pop_node":
            detail['undergrad_pop'] = item['c.name']
        if item['c'][0] == "grad_pop_node":
            detail['grad_pop'] = item['c.name']
        if item['c'][0] == 'grad_rate_node':
            detail['grad_rate'] = item['c.name']
        if item['c'][0] == 'fresh_ret_node':
            detail['fresh_ret_rate'] = item['c.name']
        if item['c'][0] == 'emp_rate_node':
            detail['emp_rate'] = item['c.name']

    data = {
        "title_info": {
            'main_title': name,
            'duration': '4-Years',
            'school_type': detail.get('setting', '') + " University",
            'location': detail.get('city', '') + ', ' + detail.get('state', ''),
            'school_link': detail.get('website', '')},
        "desc_info": {
            'title': name,
            'location': detail.get('address', '') + ' ' + detail.get('city', '') + ', ' + detail.get('state',
                                                                                                     '') + ' ' + detail.get(
                'zip', ''),
            'avg_score': {
                'reading': detail.get('read_sat', ''),
                'math': detail.get('math_sat', ''),
                'composite': detail.get('act', '')
            },
            'app_fee': detail.get('app_fee', ''),
            'expected_salary': detail.get('med_earn', ''),
            'cost': {
                'net_price': detail.get('tuition', ''),
                'avg_aid_award': detail.get('avg_aid', '')
            },
            'admission': {
                'acceptance_rate': detail.get('accept_rate', ''),
                'application_ddl': detail.get('app_dead', '')
            },
            'students': {
                'undergraduate': detail.get('undergrad_pop', ''),
                'graduate': detail.get('grad_pop', ''),
            },
            'stat': {
                'graduation_rate': detail.get('grad_rate', ''),
                'freshman_retention': detail.get('fresh_ret_rate', ''),
                'employment_rate': detail.get('emp_rate', ''),
                'median_salary': detail.get('med_earn', '')
            }
        }
    }

    return JsonResponseResult(data=data, code=200, msg='success')


def get_fame_property(request, id="asdasda"):
    logger.info("func 'get_fame_property' get a param id -> " + id)
    connection = ConnectionPool()
    result = connection.executeQuery(
        "\
        match(n)-[]-(m {name: '" + id + "'})\
        match(n)-[]-(c)\
        return labels(c) as c, c.name\
        "
    )
    detail = {}
    affil = []
    athle = []
    for item in result:
        if item['c'][0] == "president_node":
            detail['president'] = item['c.name']
        if item['c'][0] == "motto_node":
            detail['motto'] = item['c.name']
        if item['c'][0] == 'affil_node':
            affil.append(
                {'name': item['c.name'], 'link': "https://www.dbpedia.org/page/" + '_'.join(item['c.name'].split())})
        if item['c'][0] == 'athletics_node':
            athle.append(
                {'name': item['c.name'], 'link': "https://www.dbpedia.org/page/" + '_'.join(item['c.name'].split())})
        if item['c'][0] == 'mascot_node':
            detail['mascot'] = item['c.name']
        if item['c'][0] == 'school_color_node':
            detail['color'] = item['c.name']

    import requests
    from bs4 import BeautifulSoup
    url = 'https://www.colorhexa.com/color.php'
    colors = []
    if detail['color'] != 'N/A':
        col = [detail['color']]
        for color in col:
            item = color.replace('and', ',')
            item = item.replace('&', ',')
            item = item.replace(':', "")
            item = list(map(lambda s: s.strip(), item.split(',')))
            item = [i for i in item if i]
        for color in item:
            query_data = {'c': color, 'h': 'h'}
            html = requests.post(url, query_data).text
            soup = BeautifulSoup(html, 'html.parser')
            rgb = soup.find('title').string.split()[2]
            colors.append({'name': color, 'rgb': rgb})
    data = {
        "affiliations": affil,
        "athletics": athle,
        "president": {
            "name": detail.get('president', ''),
            'profile': "",
            'link': 'https://www.dbpedia.org/page/' + '_'.join(detail.get('president', 'N/A').split())
        },
        "motto": {
            'words': detail.get('motto', ''),
            'by': ""
        },
        "color": colors,
        "mascot": {
            'name': detail.get('mascot', ''),
            'logo': "",
            'link': ""
        }

    }
    return JsonResponseResult(data=data, code=200, msg='success')


def address2geo(address_str, city_str):
    import googlemaps

    gmaps = googlemaps.Client(key='AIzaSyBe0n3z7qndMX9owX_5rySTLivp7ZSMYvA')
    geocode_result = None
    if address_str == "N/A":
        geocode_result = gmaps.geocode(city_str)[0]
    else:
        geocode_result = gmaps.geocode(address_str + " " + city_str)[0]

    if geocode_result and geocode_result['geometry']:
        values = geocode_result['geometry']['location']
        return float(values['lat']), float(values['lng']),
    else:
        return float(34.052234), float(-118.243685)


def get_loc_data(request, id='asdas31asdada'):
    """

    :param request:
    :param id: you will receive a school id (str) (required)
    :return: you need to return a list of historical ranking data of this school
    {
        "markers": [
                {'label': 'School',
                 'color': 'blue',
                 'lat': '40.702147',
                 'lng': '-74.015794',
                 'size': 'normal'}
            ],
        "center": "Los Angeles, CA"
    }
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    logger.info("func 'get_ranking_data' get a param id -> " + id)
    connection = ConnectionPool()
    result = connection.executeQuery(
        "\
        match(n)-[]-(m {name: '" + id + "'})\
            match(n)-[]-(c)\
            return labels(c) as c, c.name\
            "
    )
    detail, data = {}, {}
    for item in result:
        if item['c'][0] == "addr_node":
            detail['address'] = item.get('c.name', '')
        if item['c'][0] == "city_node":
            detail['city'] = item.get('c.name', '')
        if item['c'][0] == "state_node":
            detail['state'] = item.get('c.name', '')

    center_str = detail['city'] + ", " + detail['state']
    markers = []
    if '' != detail['address']:
        lag, lng = address2geo(detail['address'], center_str)
        markers.append({
            'label': 'School',
            'color': 'orange',
            'lat': lag,
            'lng': lng,
            'size': 'normal'
        })

    data['markers'] = markers
    data['center'] = center_str

    return JsonResponseResult().ok(data=data)


def get_score_data(request, id="asdasdasdsadas"):
    """

       :param request:
       :param id: you will receive a school id (str) (required)
       :return: you need to return an obj of ACT SAT GPA data of this school
       {
        "score_data": [
            {'item': 'SAT_reading', 'niche': 67.5, 'cc': 60.3},  # div 10
            {'item': 'SAT_writing', 'niche': 64.6, 'cc': 50.6},  # div 10
            {'item': 'SAT_math', 'niche': 71.0, 'cc': 70.1},  # div 10
            {'item': 'ACT', 'niche': 64, 'cc': 68},  # * 2
            {'item': 'GPA', 'niche': 76, 'cc': 74}  # * 20
        ],
        "score_desc": {
            'niche': {
                'sat_range': '1390-1540',
                'act_range': '32-35',
            },
            'cc': {
                'sat': {
                    'reading': 731,
                    'writing': 656,
                    'math': 731,
                },
                'act': 32,
                'gpa': 3.72
            }
        }
      }
       and use JsonResponseResult().ok(data=data) return
       if there is any exception raised,
       use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
       """
    logger.info("func 'get_score_data' get a param id -> " + id)
    connection = ConnectionPool()
    result = connection.executeQuery(
        "\
        match(n)-[]-(m {name: '" + id + "'})\
        match(n)-[]-(c)\
        return labels(c) as c, c.name\
        "
    )

    detail = {}
    for item in result:
        if item['c'][0] == "read_sat_node":
            if item['c.name'] != 'N/A':
                detail['read_sat'] = item['c.name']
                detail['read'] = item['c.name']
            else:
                detail['read_sat'] = '0'
                detail['read'] = 'N/A'

        if item['c'][0] == "math_sat_node":
            if item['c.name'] != 'N/A':
                detail['math_sat'] = item['c.name']
                detail['math'] = item['c.name']
            else:
                detail['math_sat'] = '0'
                detail['math'] = 'N/A'
        if item['c'][0] == "write_sat_node":
            if item['c.name'] != 'N/A':
                detail['write_sat'] = item['c.name']
                detail['write'] = item['c.name']
            else:
                detail['write_sat'] = '0'
                detail['write'] = 'N/A'
        if item['c'][0] == "act_node":
            if item['c.name'] != 'N/A':
                detail['act'] = item['c.name']
                detail['ACT'] = item['c.name']
            else:
                detail['act'] = '0'
                detail['ACT'] = 'N/A'
        if item['c'][0] == "gpa_node":
            if item['c.name'] != 'N/A':
                detail['gpa'] = item['c.name']
                detail['GPA'] = item['c.name']
            else:
                detail['gpa'] = '0'
                detail['GPA'] = 'N/A'

    data = {
        "score_data": [
            {'item': 'SAT_reading', 'score': int(detail['read_sat']) / 10},  # div 10
            {'item': 'SAT_writing', 'score': int(detail['write_sat']) / 10},  # div 10
            {'item': 'SAT_math', 'score': int(detail['math_sat']) / 10},  # div 10
            {'item': 'ACT', 'score': int(detail['act']) * 2},  # * 2
            {'item': 'GPA', 'score': int(float(detail['gpa']) * 20)}  # * 20
        ],
        "score_desc": {
            'cc': {
                'sat': {
                    'reading': detail.get('read', ''),
                    'writing': detail.get('write', ''),
                    'math': detail.get('math', ''),
                },
                'act': detail.get('ACT', ''),
                'gpa': detail.get('GPA', '')
            }
        }
    }
    return JsonResponseResult().ok(data=data)


def get_subject_info_data(request, id="asdasdasdsadas"):
    """

       :param request:
       :param id: you will receive a school id (str) (required)
       :return: you need to return an obj of ACT SAT GPA data of this school
       {
            "niche_ranking": [
                {'item': 'Academic', 'score': 4, 'label': 'A'},
                {'item': 'Academic2', 'score': 4, 'label': 'A'},
                {'item': 'Academic3', 'score': 4, 'label': 'A'},
                {'item': 'Academic4', 'score': 4, 'label': 'A'},
                {'item': 'Academic5', 'score': 4, 'label': 'A'},
            ],
            "over_all_ranking": "A+",
            "title_list": [
                {'item': "National University", 'ranking': 24, 'desc': 'ssssssssssssssssssssssssssss'},
                {'item': "Best College for Veterans", 'ranking': 8, 'desc': 'ssssssssssssssssssssssssssss'},
                {'item': "Best Value Schools", 'ranking': 60, 'desc': 'ssssssssssssssssssssssssssss'},
                {'item': "Top Performers on Social Mobility", 'ranking': 161, 'desc': 'ssssssssssssssssssssssssssss'},
            ]
        }
       and use JsonResponseResult().ok(data=data) return
       if there is any exception raised,
       use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
       """
    logger.info("func 'get_subject_info_data' get a param id -> " + id)
    connection = ConnectionPool()
    result = connection.executeQuery(
        "match(node_school)-[:ID]->(n {name: '" + id + "'})\
        match(node_school)-[p:HAS_GRADE]->(node_n_grade)\
        return node_school.name, node_n_grade.name, p.grade"
    )

    result2 = connection.executeQuery(
        "match(node_school)-[:ID]->(n {name: '" + id + "'})\
        match(node_school)-[p:HAS_RANK]->(node_usn_rank)\
        return node_school.name, node_usn_rank.name, p.rank"
    )
    grade = {'A+': 5.0, 'A': 5.0, 'A-': 4.7, 'B+': 4.3, 'B': 4.0, 'B-': 3.7, 'C+': 3.3, \
             'C': 3.0, 'C-': 2.7, 'D+': 2.3, 'D': 2.0, 'D-': 1.7, 'F': 1.0, 'NG': 3.5}

    inv_grade = {v: k for k, v in grade.items()}
    niche = []
    overall_grade = 0
    for item in result:
        overall_grade += grade.get(item.get('p.grade', ''), '')
        if item.get('node_n_grade.name', '') in ['Academics', 'Athletics', 'Student Life', 'Party Scene', 'Safety']:
            niche.append({'item': item.get('node_n_grade.name', ''), 'score': grade.get(item.get('p.grade', ''), ''),
                          'label': item.get('p.grade', '')})

    overall_grade /= 12
    overall_rank = ""
    overall_grade = round(overall_grade, 2)
    for k, v in inv_grade.items():
        if overall_grade >= k:
            overall_rank = v
            break

    usn_rank = []
    for item in result2:
        usn_rank.append({'item': item.get('node_usn_rank.name', ''), 'ranking': int(item.get('p.rank', '0'))})

    data = {
        "niche_ranking": niche,
        "over_all_ranking": overall_rank,
        "title_list": usn_rank
    }
    return JsonResponseResult().ok(data=data)


def get_popular_major(request, id='asdas31asdada'):
    """

    :param request:
    :param id: you will receive a school id (str) (required)
    :return: you need to return a list of popular majors of this school
    10 tags will look good on the page.
    [{
        'name': "Computer Science"
    },{},...]
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """

    logger.info("func 'get_popular_major' get a param id -> " + id)
    connection = ConnectionPool()
    result = connection.executeQuery(
        "\
        match(n)-[]-(m {name: '" + id + "'})\
        match(n)-[]-(c)\
        return labels(c) as c, c.name\
        "
    )

    detail = []
    for item in result:
        if item['c'][0] == "n_pop_majors_node":
            detail.append(item['c.name'])
    data = []
    for major in detail:
        data.append({'name': major})

    return JsonResponseResult().ok(data=data)


def get_similar_school_data(request, id='asdas31asdada'):
    """

    :param request:
    :param id: you will receive a school id (str) (required)
    :return: you need to return a list of similar school of this school
    [{
        'id': 1,
        'name': 'University Of Southern California1',
        'similarity': '96%', 'link': '',
        'rating': {
            'Niche': 5,
            'CC': 3
        }

    },{},...]
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    logger.info("func 'get_similar_school_data' get a param id -> " + id)
    data = [
        {
            'id': 1,
            'name': 'University Of Southern California1',
            'similarity': '96%', 'link': '',
            'rating': {
                'Niche': 5,
                'CC': 3, }
        },
        {'id': 2, 'name': 'University Of Southern California2', 'similarity': '87%', 'link': '',
         'rating': {'Niche': 5, 'CC': 3, }},
        {'id': 3, 'name': 'University Of Southern California3', 'similarity': '86%', 'link': '',
         'rating': {'Niche': 5, 'CC': 3, }},
        {'id': 4, 'name': 'University Of Southern California4', 'similarity': '86%', 'link': '',
         'rating': {'Niche': 5, 'CC': 3, }},
        {'id': 5, 'name': 'University Of Southern California5', 'similarity': '76%', 'link': '',
         'rating': {'Niche': 5, 'CC': 3, }},
        {'id': 6, 'name': 'University Of Southern California6', 'similarity': '66%', 'link': '',
         'rating': {'Niche': 5, 'CC': 3, }},
        {'id': 7, 'name': 'University Of Southern California7', 'similarity': '66%', 'link': '',
         'rating': {'Niche': 5, 'CC': 3, }}

    ]
    return JsonResponseResult().ok(data=data)


def get_sentimental_tags(request, id=""):
    global review_tags
    logger.info("func 'get_sentimental_tags' get a param id -> " + id)
    if not review_tags:
        with open("./niche_reviews_result.json", 'r', encoding='utf-8') as file:
            review_tags = json.load(file)

    default_data = {
        "positive_info": {
            "data": [{"name": "helpful", "value": 16}, {"name": "good", "value": 15}, {"name": "nice", "value": 11},
                     {"name": "great", "value": 10}, {"name": "diverse", "value": 8}, {"name": "easy", "value": 8},
                     {"name": "amazing", "value": 8}, {"name": "first year", "value": 7}, {"name": "more", "value": 6},
                     {"name": "great school", "value": 6}, {"name": "able", "value": 5},
                     {"name": "make sure", "value": 5},
                     {"name": "convenient", "value": 5}, {"name": "friendly", "value": 5}, {"name": "most", "value": 5},
                     {"name": "other", "value": 4}, {"name": "great professor", "value": 4},
                     {"name": "knowledgeable", "value": 4}, {"name": "supportive", "value": 4},
                     {"name": "affordable", "value": 4}, {"name": "fun", "value": 4}, {"name": "much", "value": 4},
                     {"name": "feel safe", "value": 4}, {"name": "sure", "value": 3},
                     {"name": "online course", "value": 3},
                     {"name": "first semester", "value": 3}, {"name": "different", "value": 3},
                     {"name": "diverse campus", "value": 3}, {"name": "other university", "value": 3},
                     {"name": "great opportunity", "value": 3}, {"name": "passionate", "value": 3},
                     {"name": "willing", "value": 3}, {"name": "only thing", "value": 3},
                     {"name": "overall", "value": 3},
                     {"name": "great experience", "value": 3}, {"name": "nervous", "value": 3},
                     {"name": "beautiful campus", "value": 3}, {"name": "welcoming", "value": 3},
                     {"name": "good experience", "value": 3}, {"name": "grateful", "value": 2}],
            "people": {"alum": "5.8%", "other": "10.0%", "senior": "16.7%", "junior": "16.7%", "sophomore": "25.0%",
                       "freshman": "25.8%"}, "percent": "50.0%", "total": "120"},
        "negative_info": {
            "data": [{"name": "expensive", "value": 9}, {"name": "good", "value": 6}, {"name": "terrible", "value": 5},
                     {"name": "bad", "value": 5}, {"name": "greek life", "value": 4},
                     {"name": "financial aid", "value": 4},
                     {"name": "great", "value": 4}, {"name": "little", "value": 4}, {"name": "okay", "value": 4},
                     {"name": "good luck", "value": 4}, {"name": "horrible", "value": 3},
                     {"name": "boring", "value": 3},
                     {"name": "social life", "value": 3}, {"name": "bad part", "value": 3},
                     {"name": "cold", "value": 3},
                     {"name": "nice", "value": 3}, {"name": "free", "value": 3}, {"name": "fun", "value": 3},
                     {"name": "amazing", "value": 3}, {"name": "much", "value": 3}, {"name": "many", "value": 3},
                     {"name": "difficult", "value": 3}, {"name": "available", "value": 3}, {"name": "hard", "value": 3},
                     {"name": "motivated", "value": 2}, {"name": "helpful", "value": 2}, {"name": "high", "value": 2},
                     {"name": "willing", "value": 2}, {"name": "many people", "value": 2},
                     {"name": "convenient", "value": 2}, {"name": "own fun", "value": 2},
                     {"name": "next semester", "value": 2}, {"name": "sunny", "value": 2},
                     {"name": "many option", "value": 2}, {"name": "low", "value": 2},
                     {"name": "interesting", "value": 2},
                     {"name": "right", "value": 2}, {"name": "Most", "value": 2}, {"name": "well", "value": 2},
                     {"name": "few", "value": 2}],
            "people": {"other": "2.5%", "alum": "10.0%", "senior": "18.3%", "junior": "20.0%", "sophomore": "24.2%",
                       "freshman": "25.0%"}, "percent": "50.0%", "total": "120"}}
    result = review_tags.get(id, default_data)
    return JsonResponseResult().ok(data=result)
