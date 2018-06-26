# encoding:utf8
__auth__ = 'wsj'


from app.lib import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'my book is fluent python'