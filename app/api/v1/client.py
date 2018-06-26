# encoding:utf8
__auth__ = 'wsj'

from flask import request
from app.lib import Redprint
from app.validators.forms import ClientForm, EmailClientForm, ClientTypeEnum
# from app.lib.enums import ClientTypeEnum
from app.models.user import User

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)

    if form.validate():
        print ClientTypeEnum.USER_EMAIL
        print 1111111111
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        print form.type
        promise[form.type.data]()
    return 'success'


def __register_user_by_email():
    form = EmailClientForm(data=request.json)

    if form.validate():
        User.register_by_email(nickname=form.nickname.data, account=form.account.data, secret=form.secret.data)
        print 'regiested!'
    print form.errors