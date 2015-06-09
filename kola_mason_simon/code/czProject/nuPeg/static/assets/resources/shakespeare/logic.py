import sys


def filesToDict(listOfFiles):
    """
    >>> sorted(filesToDict(['test/testRead1.txt','test/testRead2.txt']).items())
    [('test/testRead1.txt', 'one\\ntwo\\n'), ('test/testRead2.txt', 'three\\nfour\\nthree\\n')]
    """
    result = {}
    for f_name in listOfFiles:
        with open(f_name) as f_obj:
            result[f_name] = f_obj.read()
    return result
    #- return {f: open(f).read() for f in listOfFiles}


def freqAnalyzer(content, keyword):
    """
    >>> sorted(freqAnalyzer({'test/testRead1.txt': 'one\\ntwo\\n',
    ...                      'test/testRead2.txt': 'three\\nfour\\nthree\\n'},
    ...                     'tHree').items())
    [('test/testRead1.txt', 0), ('test/testRead2.txt', 2)]

    >>> sorted(freqAnalyzer(filesToDict(['test/testRead1.txt','test/testRead2.txt']),
    ...                     'tHree').items())
    [('test/testRead1.txt', 0), ('test/testRead2.txt', 2)]
    """
    return {opusName: content.lower().count(keyword.lower())
            for opusName, content in content.items()}

# Bonus (needed for Bootstrap): new frequency analyser which includes percentages.


def freqAnalyserNorm(content, keyword):
    """
    >>> sorted(freqAnalyserNorm({'1.txt': 'one\\ntwo\\n',
    ...                          '2.txt': 'three\\nfour\\nthree\\n'},
    ...                         'tHree').items())
    [('1.txt', (0, 0.0)), ('2.txt', (2, 100.0))]

    >>> sorted(freqAnalyserNorm({'1.txt': 'one\\ntwo\\nthree\\nTHREE\\nthree\\n',
    ...                          '2.txt': 'three\\nfour\\nthree\\n'},
    ...                         'tHree').items())
    [('1.txt', (3, 100.0)), ('2.txt', (2, 66.66666666666667))]
    """
    corpus = freqAnalyzer(content, keyword)
    maxValue = max(corpus.values())
    percent = 0 if maxValue == 0 else 100.0/maxValue

    return {opusName: (corpus[opusName], corpus[opusName]*percent)
            for opusName, content in corpus.items()}


def freqAnalyserStacked(content, *keywords):
    """
    >>> sorted(freqAnalyserStacked({'1.txt': 'one\\ntwo\\nthree\\n',
    ...                      '2.txt': 'three\\nfour\\nthree\\ntwo\\n'},
    ...                       'tHree', 'Two').items())
    [('1.txt', [(1, 50.0), (1, 100.0)]), ('2.txt', [(2, 100.0), (1, 100.0)])]
    """
    corpusList = [freqAnalyzer(content, k) for k in keywords]
    maxValueList = [max(corpus.values()) for corpus in corpusList]
    percentList = [0 if m == 0 else 100.0/sum(maxValueList) for m in maxValueList]
    
    return {opusName: [(corpus[opusName],
                        corpus[opusName]*percentList[i]) for i,
                        corpus in enumerate(corpusList)]
            for opusName, content in content.items()}

# Don't need a main().

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
