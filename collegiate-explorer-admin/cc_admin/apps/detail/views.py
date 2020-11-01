import logging

from JsonResponseResult import JsonResponseResult

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
    data = {
        "title_info": {
            'main_title': "University of Southern California (USC)",
            'duration': '4-Years',
            'school_type': "Private University",
            'location': "Los Angeles, CA",
            'school_link': "http://www.usc.edu"},
        "desc_info": {
            'title': "University of Southern California",
            'location': "University Park Los Angeles, CA 90089",
            'avg_score': {
                'reading': "700",
                'math': "714",
                'composite': "32"
            },
            'expected_salary': "74,000",
            'cost': {
                'net_price': '36,161',
                'national': "15,523",
                'financial_aid': "69%",
                'avg_aid_award': "35,953"
            },
            'stat': {
                'graduation_rate': "69%",
                'freshman_rentention': "69%",
                'employment_rate': "69%",
                'median_salary': "120,000",
            },
            'admission': {
                'acceptance_rate': '13%',
                'application_ddl': 'Jan. 15th'
            },
            'students': {
                'undergraduate': "20,048",
                'graduate': "27,970",
                'international': "2,499"
            }
        }
    }
    return JsonResponseResult(data=data, code=200, msg='success')


def get_fame_property(request, id="asdasda"):
    logger.info("func 'get_fame_property' get a param id -> " + id)
    data = {
        "affiliations": [
            {
                'name': "University System of Georgia",
                'link': "",  # for now, we dont have url,
                # but we might have it later or at leasr we need to pretend we have
                # i'd like to call it extendibility. hahah
            }, {
                'name': "Southern Intercollegiate Athletics Conference",
                'link': "",
            }
        ],
        "athletics": [
            {
                'name': "NCAA Division II",
                'link': ""
            },
        ],
        "president": {
            "name": "Joe Biden",
            'profile': "",
            'link': ""
        },
        "motto": {
            'words': "Let there be light",
            'by': ""
        },
        "color": [
            {
                'name': " Green",
                'rgb': "#40FF50"
            }, {
                'name': "White",
                'rgb': "#1e90ff"
            }
        ],
        "mascot": {
            'name': "Grizzly Bear",
            'logo': "",
            'link': ""
        }

    }
    return JsonResponseResult(data=data, code=200, msg='success')


def get_ranking_data(request, id='asdas31asdada'):
    """

    :param request:
    :param id: you will receive a school id (str) (required)
    :return: you need to return a list of historical ranking data of this school
    [{
        'name': '1997',
        'value': 37,
        'type': 'Niche'
    },{},...]
    and use JsonResponseResult().ok(data=data) return
    if there is any exception raised,
    use JsonResponseResult().error(data=[], msg="explain your error", code="500") return
    """
    logger.info("func 'get_ranking_data' get a param id -> " + id)
    data = [{'name': 1997, 'value': 37, 'type': 'Niche'},
            {'name': 2007, 'value': 35, 'type': 'Niche'},
            {'name': 2018, 'value': 30, 'type': 'Niche'},
            {'name': 2020, 'value': 33, 'type': 'Niche'},
            {'name': 1997, 'value': 40, 'type': 'CollegeConfidential'},
            {'name': 2007, 'value': 36, 'type': 'CollegeConfidential'},
            {'name': 2018, 'value': 35, 'type': 'CollegeConfidential'},
            {'name': 2020, 'value': 39, 'type': 'CollegeConfidential'},
            {'name': 1997, 'value': 30, 'type': 'QS News'},
            {'name': 2007, 'value': 32, 'type': 'QS News'},
            {'name': 2018, 'value': 35, 'type': 'QS News'},
            {'name': 2020, 'value': 32, 'type': 'QS News'}]
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
    data = {
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
    data = [
        {'name': "Computer Science"},
        {'name': "Data Science"},
        {'name': "Business Administration"},
        {'name': "Biological Sciences"},
        {'name': "Chemistry"},
        {'name': "Environmental Engineering"},
        {'name': "Social Sciences"},
        {'name': "Human Development and Aging"},
        {'name': "Biomedical Engineering"},
        {'name': "Natural Sciences"}]
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
