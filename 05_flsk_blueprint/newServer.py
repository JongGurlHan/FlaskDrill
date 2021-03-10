from flask import Flask
from subFolder import blueprint_test

app = Flask(__name__)

app.register_blueprint(blueprint_test.test, prefix ='/test')

if __name__ == '__main__':
    app.run(port='8090')