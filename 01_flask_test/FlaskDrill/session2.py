from flask import Flask, url_for, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = "random secret key"

@app.route('/')
def index():
    if 'username' in session:
       username = session['username']
       return username +" logged!" +\
       "<p>" "<a href='/logout'>Logout Page</a>" "</p>"

    return "you need to login" "<p>" "<a href='/login2'>Login Page</a>" "</p>"


@app.route('/login2', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        username = session['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))
    
    
    


if __name__ == '__main__':
    app.run(port=5008, debug=True)