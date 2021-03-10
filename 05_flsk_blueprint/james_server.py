from flask import Flask
from sub_blueprint import blog_test

app = Flask(__name__)
app.register_blueprint(blog_test.blog_ab, url_prefix='/test')  #url_prefix = 기본경로명 
                                                               #하위폴더의 소스파일에 있는 라우팅 경로는 URL/기본경로명/라우팅경로 와 같이 설정됨

if __name__ == '__main__':
    app.run(port='8080')