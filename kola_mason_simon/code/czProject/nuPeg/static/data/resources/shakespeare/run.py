from flask import Flask, render_template
import glob

import logic

app = Flask(__name__)

listOfFiles = glob.glob('data/*')
corpus = logic.filesToDict(listOfFiles)

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/search/<term>')
def search(term):
    items = sorted((play.rsplit('/', 1)[-1], freq, norm) for play,
      (freq, norm) in logic.freqAnalyserNorm(corpus, term).iteritems())
    return render_template('bootstrap.html', # 'results.html'
                           term=term,
                           items=items)

app.run(host='0.0.0.0', port=8080, debug=True)
