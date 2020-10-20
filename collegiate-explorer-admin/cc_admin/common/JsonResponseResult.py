import json

from django.http import HttpResponse


class JsonResponseResult(HttpResponse):

    def __init__(self, code=None, msg=None, data=None, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        self.data = {"code": code,
                     "msg": msg,
                     "data": data}
        super().__init__(content=json.dumps(self.data),  **kwargs)
