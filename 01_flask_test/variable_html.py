from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html', name = user)


if __name__ == "__main__":
    app.run(port='8090')