from JsonResponseResult import JsonResponseResult
from Neo4jConnectionPool import ConnectionPool
import logging

logger = logging.getLogger('django')


def index(request):
    return JsonResponseResult().ok(data="asdasdas")


def top10(request):
    connection = ConnectionPool()
    # result = connection.executeQuery(
    #     "MATCH (cloudAtlas2 {title: $param, tagline: $param1}) RETURN cloudAtlas2",
    #     param="Cloud Atlas",
    #     param1="Everything is connected")
    result2 = connection.executeQuery(
        "MATCH (tom:Person {name: \"Tom Hanks\"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies")
    return JsonResponseResult().ok(data=result2)
    # http://127.0.0.1:8000/search/top10


def test(request):
    return JsonResponseResult().error(code=405, msg='sadasdasd', data="sssssss")


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
