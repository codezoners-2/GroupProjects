from flask import Flask, render_template, request
import glob
import logic

app = Flask(__name__)

listOfFiles = glob.glob('data/*')
corpus = logic.filesToDict(listOfFiles)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def do_search():
    if request.method == 'POST':
        term = request.form.get('term')
        items = sorted((play.rsplit('/', 1)[-1], freq, norm) for play,
                        (freq, norm) in logic.freqAnalyserNorm(corpus,
                        term).iteritems())
        if term:
            return render_template('bootstrap_formed.html',
                                    term=term,
                                    items=items)
            # Display search results
        else:
            return render_template('bootstrap_formed.html')
            # Show search form only
    else:
        return render_template('bootstrap_formed.html')
        # Show search form only

app.run(host='0.0.0.0', port=8080, debug=True)
