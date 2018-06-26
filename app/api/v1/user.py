# encoding:utf8
__auth__ = 'wsj'

from app.lib import Redprint

api = Redprint('user')

@api.route('/get')
def get_user():
    return 'my name is wsj'
