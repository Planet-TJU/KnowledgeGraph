from flask import Flask, render_template, request, jsonify, json

from ShowKnowledge.neodb.robot_answer import get_robot_answer
from ShowKnowledge.neodb.query_graph import query, get_details

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/query_node', methods=['GET', 'POST'])
def query_node():
    return render_template('query_node.html')


@app.route('/answer_robot', methods=['GET', 'POST'])
def answer_robot():
    return render_template('answer_robot.html')


@app.route('/search_node', methods=['GET', 'POST'])
def search_node():
    name = request.args.get('name')
    json_data = query(str(name))
    return jsonify(json_data)


@app.route('/get_chart', methods=['GET', 'POST'])
def get_chart():
    node_or_edge = json.loads(request.form.get('type'))  # $.ajax传多个参数只能post请求，对应form
    data = json.loads(request.form.get('data'))
    nodes = json.loads(request.form.get('nodes'))
    json_data = get_details(node_or_edge, data, nodes)
    return jsonify(json_data)


@app.route('/dialogue_answer', methods=['GET', 'POST'])
def dialogue_answer():
    question = request.args.get('text')
    ans = get_robot_answer(str(question))
    json_data = {'data': ans}
    json_data['data'].replace("\n", "<br/>")
    return jsonify(json_data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
