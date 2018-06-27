# encoding:utf8
from wtforms import Form
from app.lib.error import ParamIllegalException
from flask import request

class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        form = super(BaseForm, self)
        if not form.validate():
            raise ParamIllegalException(form.errors)
        return self