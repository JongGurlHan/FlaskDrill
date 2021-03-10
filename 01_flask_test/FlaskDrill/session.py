from flask import Flask, request, session, redirect, url_for,render_template

app = Flask(__name__)
app.secret_key = 'any random string' #세션을 사용하기 위해선 설정해야한다. 

#플라스크에선 세션은 딕셔너리의 형태로 저장되며 키를 통해 해당 값을 불러올 수 있다. 
@app.route('/')
def index():
    if 'username' in session: #session 안에 'username'이 있다면 
        username  = session['username'] # session 딕셔너리의 'username'키를 통해 불러진 값을 변수 username에 대입한다
        return 'Logged in as '+ username + '<br>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"
    
    return "You're not logged in <b> <a href = '/login'></b>" + \
        "click here to log in </b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('login.html')

@app.route('/logout')
def logout():
    #remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5007, debug=True)