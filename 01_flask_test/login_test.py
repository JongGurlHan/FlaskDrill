from flask import Flask, jsonify, request, render_template
app = Flask(__name__, static_url_path= '/static')

@app.route('/login')
def login():
    email_address = request.args.get('email_address')
    password = request.args.get('pw')
   
    print(email_address, password)

    if email_address == 'gojkhan@naver.com':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth' : 'fail'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    return render_template('login_rawtest.html')



if __name__ == '__main__':
    app.run(port = 8090, debug=True)