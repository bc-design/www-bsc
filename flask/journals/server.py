from flask import Flask, render_template, make_response, request
app = Flask(__name__)

import string
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
	print 'I got clicked! The server is working!' #testing
	return 'The server is working!'

@app.route('/', methods=['POST'])
def my_form_post():
	# starts the journal lookup app with user-defined input
	print 'app started with form!' #testing
	text = request.form['text']
	outstyle = request.form['outstyle']
	print 'Output Style: ', outstyle #testing
	try:
		results = journal_lookup.main(dir,text)
	except:
		print "Unexpected error:", sys.exc_info()[0] #testing
		print traceback.format_exc() #testing
	# prepare the response for returning
	if outstyle == 'csv':
		response = make_response(string.join(results,"\n"))
		response.headers["Content-Disposition"] = "attachment; filename=journal_info.csv"
	elif outstyle == 'html':
		response = make_response(string.join(results,"<br />"))
	return response

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
