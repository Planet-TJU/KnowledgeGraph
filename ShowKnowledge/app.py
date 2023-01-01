from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/query_node', methods=['GET', 'POST'])
def search_page():
    return render_template('query_node.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
