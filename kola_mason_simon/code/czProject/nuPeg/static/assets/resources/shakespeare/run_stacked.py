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
        terms = [request.form.get('term'+str(i+1))
                for i in xrange(3) if request.form.get('term'+str(i+1))]
        items = sorted((play.rsplit('/', 1)[-1], dataList) for play,
                    dataList in logic.freqAnalyserStacked(corpus,
                    *terms).iteritems())
        if any(terms):
            return render_template('bootstrap_stacked.html',
                                    terms=terms,
                                    items=items)
            # Display search results
        else:
            return render_template('bootstrap_stacked.html')
            # Show search form only
    else:
        return render_template('bootstrap_stacked.html')
        # Show search form only

app.run(host='0.0.0.0', port=8080, debug=True)
