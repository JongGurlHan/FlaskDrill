#routes.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask App!'

@app.route('/user/')
def hello():
    users = ["James", "David", "Richard", "Jay"]
    var =1
    return render_template('user.html', **locals())


@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return 'User %s' %username


@app.route('/user/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return 'Post %d' %post_id 



@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)




if __name__ == '__main__':
    app.run(debug=False)