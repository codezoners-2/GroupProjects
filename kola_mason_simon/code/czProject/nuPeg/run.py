from flask import Flask, render_template, jsonify, request
import random
import logic

app = Flask(__name__)
#listOfFiles = os.listdir("data")
#newList = map(lambda x: "data/" + x, listOfFiles)
corpus = logic.filesToDict("static/imageLinks.txt")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/play', methods=['GET', 'POST'])
def play():
    num = 1
    return render_template('play.html', x=random.randint(0, 9), q=num)


@app.route('/playResult', methods=['GET', 'POST'])
def playResult():
    question = request.form.get('imageText')
    answer = request.form.get('number')
    return render_template('playResult.html',
                           x=question,
                           y="You entered %s" % answer,
                           result="Your answer is: " + validate(question, answer))


def validate(x, y):
    if x == y:
        return "Correct"
    else:
        return "Incorrect"


@app.route('/fetch')
def fetch():
    #resp = jsonify({'result': corpus.values()[random.randint(0,len(corpus)-1)]})
    #resp.status_code = 200
    resp = jsonify({'result': random.choice(corpus.values())})
    return resp

app.run(host='0.0.0.0', port=8080, debug=True)
