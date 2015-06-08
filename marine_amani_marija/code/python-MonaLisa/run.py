3
from flask import Flask, render_template, jsonify


import json
import pprint

from collections import OrderedDict
from datetime import date
app = Flask(__name__)
bigRes = {}
mo = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def read_file():
	# filter empty lines and remove headers
	lines = filter(None, open('aberporthdata.txt', 'r').read().splitlines())[7:]
	elements = ['tmax', 'tmin', 'af', 'rain', 'sun', 'prov']
	tminmin = 1000
	tminmax= -1000
	tmaxmin= 1000
	tmaxmax = -1000
	rainmin = 0
	rainmax = 0 

	data = {}

	for line in lines:
		content = line.split()

		# if provisional is not present, add it
		if len(content) < 8:
			content.append('Non Provisional')

		year, month = map(int, content[:2])
		record = {element: content[i+2] for i, element in enumerate(elements)}
		if record['tmin'] != '---':
			if tminmin > float(record['tmin']):
				tminmin = float(record['tmin'])
			if tminmax < float(record['tmin']):
				tminmax = float(record['tmin'])
		if record['tmax']!= '---':
			if tmaxmin > float(record['tmax']):
				tmaxmin = float(record['tmax'])	
			if tmaxmax < float(record['tmax']):
				tmaxmax = float(record['tmax'])
		if record['rain']!= '---':
			if rainmin > float(record['rain']):
				rainmin = float(record['rain'])
			if rainmax < float(record['rain']):
				rainmax = float(record['rain'])  

		if not data.has_key(year):
			data[year] = []

		# get month name
		month = date(1900, month, 1).strftime('%b').lower()
		data[year].append({month: record})
		#get max of all temperatures
		

	# store result in list
	res = []
	

	# order by year
	ordered_data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
	res = [{'year': year, 'months': months} for year, months in ordered_data.items()]
	# print 'overall min temperature:' + str(tmin)
	# print 'overall max temperature:' + str(tmax)
	# print 'min rain:' + str(rainmin)
	# print 'max rain:' + str(rainmax)
	bigRes['stats']=res
	bigRes['tmaxmin'] = tmaxmin
	bigRes['tmaxmax'] = tmaxmax
	bigRes['tminmin'] = tminmin
	bigRes['tminmax'] = tminmax

	bigRes['rainmin'] = rainmin
	bigRes['rainmax'] = rainmax
	

	with open('data2.json', 'w+') as myfile:
		myfile.write(json.dumps(bigRes))

@app.route('/getData')
def getData():
	numOfYears = len(bigRes['stats'])
	

	while (len(bigRes['stats'][numOfYears-1]['months'])<12):
		tempEntry = {}
		monthMissing = len(bigRes['stats'][numOfYears-1]['months'])
		tempEntry[mo[monthMissing]] = {}
		tempEntry[mo[monthMissing]]['af']="---"
		tempEntry[mo[monthMissing]]['prov']="Non Provisional"
		tempEntry[mo[monthMissing]]['sun']="---"
		tempEntry[mo[monthMissing]]['tmax']="---"
		tempEntry[mo[monthMissing]]['tmin']="---"
		bigRes['stats'][numOfYears-1]['months'].append(tempEntry)
	
	return jsonify(bigRes)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
	read_file()
	app.run()

