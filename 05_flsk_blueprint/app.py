from flask import Flask
import blue

app = Flask(__name__)

#blue.py와 bp객체를 app객체에 적용
#임포트한파일명.블루프린트객체
app.register_blueprint(blue.bp)
app.register_blueprint(blue.bp2)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run(port='8080')