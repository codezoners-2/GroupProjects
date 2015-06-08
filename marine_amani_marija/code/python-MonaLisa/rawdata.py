import json
from pprint import pprint
from StringIO import StringIO

with open('data2.json') as data_file:    
	data = json.load(data_file)
	print data['year']
# pprint(data)