from flask import Flask, render_template, jsonify
import os, random
import logic

app = Flask(__name__)

@app.route('/page/<name>')
def page(name):
    return render_template('index.html', name=name)

@app.route('/data/simple/<int:counter>')
def simple(counter):
    print("COUNTER", counter)
    return jsonify({'result': [{'rgb': [0, 0, 0],
                                'x': 0.5,
                                'y': 0.5,
                                'r': 1,
                                'key': counter}]})

@app.route('/data/stack/<int:counter>')
def stack(counter):
    return jsonify({'result': logic.makeStack(counter)})

@app.route('/data/dots/<int:counter>')
def dots(counter):
    return jsonify({'result': logic.makeDots(counter)})

app.run(host='0.0.0.0', port=8080, debug=True)
