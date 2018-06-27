# encoding:utf8
__auth__ = 'wsj'

from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from wtforms.validators import ValidationError
from app.models.user import User
from app.validators.base import BaseForm
from ..lib.enums import ClientTypeEnum
from enum import Enum


# class ClientTypeEnum():
#
#     USER_EMAIL = 100
#     USER_MOBILE = 101
#     USER_MINA = 200
#     USER_WX = 201
#
#     def __call__(self, type):
#         for attr in dir(self):
#             value = getattr(self, attr, None)
#             if value == type:
#                 self.name = attr
#                 self.value = value
#                 return self
#         print 123
#         raise ValueError


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            # client = ClientTypeEnum[value.data]
            client = int(value.data)
            assert client in [100, 101, 200, 201]
        except ValueError as e:
            self.errors['type'] = u'type不合法'
            raise ValidationError
        except AssertionError as e:
            self.errors['type'] = u'type不合法'
            raise ValidationError
        self.type.data = client


class EmailClientForm(ClientForm):
     account = StringField(validators=[
         Email(message='invalidate email')
     ])
     secret = StringField(validators=[
         DataRequired(),
         Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}')
     ])

     nickname = StringField(validators=[
         DataRequired(),
         length(min=2, max=22)
     ])

     def validate_account(self, value):

         if User.query.filter_by(email=value.data).first():
             raise ValidationError()
