import json

from django.http import HttpResponse


class JsonResponseResult(HttpResponse):

    def __init__(self, data=None, code=None, msg=None, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        if not data: data = list()
        self.data = {"code": code,
                     "msg": msg,
                     "data": data}
        super().__init__(content=json.dumps(self.data), **kwargs)

    def error(self, data, code=404, msg='ERROR', **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        self.__init__(data=data, code=code, msg=msg, **kwargs)
        return self

    def ok(self, data, code=200, msg='OK', **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        self.__init__(data=data, code=code, msg=msg, **kwargs)
        return self
