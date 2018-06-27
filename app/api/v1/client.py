# encoding:utf8
__auth__ = 'wsj'

from flask import request
from app.lib import Redprint
from app.lib.error import APIRequestException, ParamIllegalException, Success
from app.validators.forms import ClientForm, EmailClientForm, ClientTypeEnum
# from app.lib.enums import ClientTypeEnum
from app.models.user import User


api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    1/0
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = EmailClientForm().validate_for_api()
    User.register_by_email(nickname=form.nickname.data, account=form.account.data, secret=form.secret.data)

    print form.errors