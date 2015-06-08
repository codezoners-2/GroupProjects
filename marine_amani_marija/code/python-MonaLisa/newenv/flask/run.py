from flask import Flask, render_template

app = Flask(__name__)

corpus = None

# You need to build the 'corpus' of works: this doesn't change once the server
# is up and running. You have the code to do this already.

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/search/<term>')
def search(term):
    items = None
    # Think about what "items" needs to be in order to render it in a template.
    # Obviously it needs to contain a sequence of play names paired with integers
    # (word count) - it's built from the corpus.
    # You have the code to do the actual calculation already.
    return render_template('results.html',
                           term=term,
                           items=items)

app.run(host='0.0.0.0', port=8080, debug=True)
