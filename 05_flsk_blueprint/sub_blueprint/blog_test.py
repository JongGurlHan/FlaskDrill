 #blog_test.py
from flask import Blueprint

blog_ab = Blueprint('blog', __name__)

#http://localhost:8080/blog/blog1
@blog_ab.route('/blog1')
def blog():
    return 'TEST BLUEPRINT'

@blog_ab.route('/blog2')
def blog2():
    return 'TEST BLUEPRINT'