from JsonResponseResult import JsonResponseResult
import logging

logger = logging.getLogger('django')


def get_basic_info(request, id='2005'):
    data = [{'id': "1",
             'name': "1",
             'gender': "1"},
            {'id': "2",
             'name': "2",
             'gender': "2"},
            {'id': "3",
             'name': "3",
             'gender': "3"}, {
                'id': str(id)
            }]
    return JsonResponseResult(data=data, code=200, msg='success')


# Done
def get_popular_major(request, id='asdas31asdada'):
    """

    :param request:
    :param id: you will receive a school id (str)
    :return: you need to return a list of popular majors of this school
    10 tags will look good on the page.
    [{
        'name': "Computer Science",
        'link': "/search?major='Computer Science'"
    },{},...]
    """

    logger.info("get a param id -> " + id)
    data = [
        {'name': "Computer Science", 'link': "/search?major='Computer Science'"},
        {'name': "Data Science", 'link': "/search?major='Data Science'"},
        {'name': "Business Administration", 'link': "/search/major='Business Administration'"},
        {'name': "Biological Sciences", 'link': "/search/major='Biological Sciences'"},
        {'name': "Chemistry", 'link': "/search/major='Chemistry'"},
        {'name': "Environmental Engineering", 'link': "/search/major='Environmental Engineering'"},
        {'name': "Social Sciences", 'link': "/search/major='Social Sciences'"},
        {'name': "Human Development and Aging", 'link': "/search/major='Human Development and Aging'"},
        {'name': "Biomedical Engineering", 'link': "/search/major='Biomedical Engineering'"},
        {'name': "Natural Sciences", 'link': "/search/major='Natural Sciences'"}]
    return JsonResponseResult().ok(data=data)


def get_ranking_data(request, id='asdas31asdada'):
    """

    :param request:
    :param id: you will receive a school id (str)
    :return: you need to return a list of historicla ranking data of this school
    [{
        'year': '1997',
        'value': 37,
        'type': 'Niche'
    },{},...]
    """
    data = [{'year': '1997', 'value': 37, 'type': 'Niche'},
            {'year': '2007', 'value': 35, 'type': 'Niche'},
            {'year': '2018', 'value': 30, 'type': 'Niche'},
            {'year': '2020', 'value': 33, 'type': 'Niche'},
            {'year': '1997', 'value': 40, 'type': 'CollegeConfidential'},
            {'year': '2007', 'value': 36, 'type': 'CollegeConfidential'},
            {'year': '2018', 'value': 35, 'type': 'CollegeConfidential'},
            {'year': '2020', 'value': 39, 'type': 'CollegeConfidential'},
            {'year': '1997', 'value': 30, 'type': 'QS News'},
            {'year': '2007', 'value': 32, 'type': 'QS News'},
            {'year': '2018', 'value': 35, 'type': 'QS News'},
            {'year': '2020', 'value': 32, 'type': 'QS News'}],
    return JsonResponseResult().ok(data=data)
