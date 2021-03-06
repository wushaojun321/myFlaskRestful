from flask import Blueprint

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    from app.api.v1 import user, book, client
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1