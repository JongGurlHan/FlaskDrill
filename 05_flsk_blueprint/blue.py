from flask import Blueprint

# url prefix 지정
# 이제 아래에 생성되는 모든 route 경로는 앞에 "/blue"가 붙게 됨
bp = Blueprint('blue', __name__, url_prefix ='/blue')
bp2 = Blueprint('blue2', __name__, url_prefix ='/blue2')

@bp.route('/1')
def print_blue1():
    return "hello blue1!"

@bp.route('/2')
def print_blue2():
    return "hello blue2!"

@bp2.route('/1')
def print_newblue1():
    return "hello new blue1!"

@bp2.route('/2')
def print_newblue2():
    return "hello new blue2!"
