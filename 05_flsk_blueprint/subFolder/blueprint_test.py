from flask import Blueprint

test = Blueprint('name', __name__)

@test.route('/test1')
def test1():
    return "test1"

@test.route('/test2')
def test2():
    return "test2"