`-*- mode: markdown; mode: visual-line; mode: adaptive-wrap-prefix; -*-`

# SIMPLE SHAKESPEARE

Build a server which takes a search term from the web page URL (of the form `localhost:8080/search/<term>`) and returns a page containing the plays listed with a count of occurrences of the term.

The `logic.py` file contains all the logic to preload the data files, and to calculate counts of terms.

Tasks:

- Read the data files in once, when the server starts, to build a "corpus" of work (filenames mapped to contents)
- In the `search` function: perform the search, getting results back from `logic.py` and the corpus. How do these results have to be processed or structured, to pass them into the template? (What is the form of the template?)
- In the template: turn the structured results into HTML
