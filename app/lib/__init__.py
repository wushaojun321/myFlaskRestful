# encoding:utf8
__auth__ = 'wsj'


class Redprint:

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((rule, f, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if not url_prefix:
            url_prefix = '/' + self.name
        for rule, f, option in self.mound:
            endpoint = option.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix+rule, endpoint, f, **option)
