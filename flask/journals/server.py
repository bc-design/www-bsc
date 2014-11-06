from flask import Flask, render_template, make_response
app = Flask(__name__)

import sys
import traceback
import journal_lookup

dir = '/var/www2/www-bsc/flask/journals/'

@app.route('/')
def hello_world():
	return render_template('template.html')
	#return 'Hello Worlds!'

@app.route('/my-link/')
def my_link():
	print 'I got clicked!'
	return 'Click.'

@app.route('/journals/')
def my_app():
	print 'app started!'
	#return 'Hello Worlds.'
	try:
		journal_lookup.main(dir)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		print traceback.format_exc()
	# We need to modify the response, so the first thing we 
	# need to do is create a response out of the CSV string
	csv = open(dir+'temp/journal_info.csv','r').read()
	response = make_response(csv)

	# This is the key: Set the right header for the response
	# to be downloaded, instead of just printed on the browser
	response.headers["Content-Disposition"] = "attachment; filename=journal_info.csv"
	return response

if __name__ == '__main__':
	app.run(debug=True)