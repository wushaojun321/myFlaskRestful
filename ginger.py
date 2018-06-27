# encoding: utf8
from app.app import create_app
from app.lib.error import APIRequestException
from werkzeug.exceptions import HTTPException

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIRequestException):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIRequestException(code=code, msg=msg, error_code=error_code)
    else:
        if app.config.get('DEBUG'):
            return e
        return APIRequestException()

if __name__ == '__main__':
    app.run(debug=True)