from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=['GET'])
def test():
    return make_response(jsonify(success=True), 200)

    #그냥 return jsonify(success=True)해도 되지만 http status code인 '200'을 명확하게 써서 넣어주려면 make_response필요하다 

if __name__ == '__main__':
    app.run(port="8082")
