# encoding:utf8
from werkzeug.exceptions import HTTPException
from flask import request, json


class APIRequestException(HTTPException):

    code = 500
    msg = 'sorry! we make a mistake'
    error_code = 999

    def __init__(self, code=None, msg=None, error_code=None, headers=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code

        super(APIRequestException, self).__init__(msg, None)

    def get_body(self, environ=None):
        res = {
            'error_code': self.error_code,
            'msg': self.msg,
            'request': str(request.full_path)
        }
        return json.dumps(res)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class ParamIllegalException(APIRequestException):
    code = 400
    msg = ''
    error_code = 1000

    def __init__(self, msg=None):
        if msg:
            self.msg = msg
        super(ParamIllegalException, self).__init__(code=None, msg=None, error_code=None, headers=None)


class Success(APIRequestException):
    code = 200
    error_code = 0
    msg = 'ok'