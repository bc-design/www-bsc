from flask import Flask, render_template, make_response, request
app = Flask(__name__)

import sys
import traceback
import journal_lookup

dir = '/var/www2/www-bsc/flask/journals/'

@app.route('/')
def hello_world():
	# renders the homepage
	return render_template('template.html')

@app.route('/my-link/')
def my_link():
	# a test link to verify that Python, Apache, and WSGI are working
	print 'I got clicked!'
	return 'The server is working!'

@app.route('/', methods=['POST'])
def my_form_post():
	# starts the journal lookup app with user-defined input
	print 'app started with form!' #testing
	text = request.form['text']
	outstyle = request.form['outstyle']
	print 'Output Style: ', outstyle #testing
	try:
		resultsvar = journal_lookup.main(dir,text)
		results = string.join(resultsvar)
	except:
		print "Unexpected error:", sys.exc_info()[0] #testing
		print traceback.format_exc() #testing

	if outstyle == 'asd': #testing
		# We need to modify the response, so the first thing we 
		# need to do is create a response out of the CSV string
		csv = open(dir+'temp/journal_info.csv','r').read()
		response = make_response(csv)
		print csv # testing		
		# This is the key: Set the right header for the response
		# to be downloaded, instead of just printed on the browser
		response.headers["Content-Disposition"] = "attachment; filename=journal_info.csv"
		return response
	elif outstyle == 'csv':
		response = make_response(results)
		response.headers["Content-Disposition"] = "attachment; filename=journal_info.csv"
		return response
	else:
		return render_template('journals.html')

if __name__ == '__main__':
	app.run(debug=True)
