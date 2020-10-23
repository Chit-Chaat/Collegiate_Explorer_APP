__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/20/2020 11:10 AM'

from neo4j import GraphDatabase
from django.conf import settings

db_configuration = settings.DATABASES['default']


class ConnectionPool:

    def __init__(self, uri=None, user=None, pwd=None):
        user = db_configuration['USER']
        pwd = db_configuration['PASSWORD']
        uri = db_configuration['URL']
        self.driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def close(self):
        self.driver.close()

    def executeQuery(self, sql=None, **kwargs):
        with self.driver.session() as session:
            result = session.read_transaction(self._executeSQL, sql, **kwargs)
            return result

    @staticmethod
    def _executeSQL(tx, sql, **kwargs):
        print("inner param->", kwargs)
        print("executed sql ->", sql)
        return tx.run(sql, **kwargs).data()
