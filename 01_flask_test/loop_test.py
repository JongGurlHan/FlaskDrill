from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/hello_loop')
def loop():
    item_list = ['item1', 'item2', 'item3']
    return render_template('loop.html', items = item_list)




if __name__ == '__main__':
    app.run(port = 8090, debug=True)