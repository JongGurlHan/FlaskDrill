from flask import Flask, render_template, request, make_response

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setCookie' ,methods = ['POST'])
def setCookie():
    user = request.form['userId']

    result = make_response("Cookie is made!")
    result.set_cookie("userId", user)
    
    return result


@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
    app.run(port=5006, debug=True)