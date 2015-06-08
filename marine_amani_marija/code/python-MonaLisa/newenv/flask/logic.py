import sys

def filesToDict(listOfFiles):
	'''
	>>> sorted(filesToDict(['test/testRead1.txt','test/testRead2.txt']).items())
	[('test/testRead1.txt', 'one\\ntwo\\n'), ('test/testRead2.txt', 'three\\nfour\\nthree\\n')]
	'''
	return {f: open(f).read() for f in listOfFiles}

def freqAnalyzer(content, keyword):
	'''
	>>> sorted(freqAnalyzer({'test/testRead1.txt': 'one\\ntwo\\n',
        ...                      'test/testRead2.txt': 'three\\nfour\\nthree\\n'},
        ...                     'tHree').items())
	[('test/testRead1.txt', 0), ('test/testRead2.txt', 2)]

	>>> sorted(freqAnalyzer(filesToDict(['test/testRead1.txt','test/testRead2.txt']),
        ...                     'tHree').items())
	[('test/testRead1.txt', 0), ('test/testRead2.txt', 2)]
	'''
	return {opusName: content.lower().count(keyword.lower()) for opusName, content in content.items()}

# Don't need a main().

if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)
