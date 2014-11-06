from flask import Flask, render_template, make_response, request
app = Flask(__name__)

import sys
import traceback
import journal_lookup

dir = '/var/www2/www-bsc/flask/journals/'

@app.route('/')
def hello_world():
	return render_template('template.html')

@app.route('/my-link/')
def my_link():
	print 'I got clicked!'
	return 'Click.'

@app.route('/journals/')
def my_app():
	print 'app started!'
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

#@app.route('/', methods=['POST'])
#def my_form_post():
#	print 'form submitted!'
#    text = request.form['text']
#    processed_text = text.upper()
#	# return the text, but upper case!
#    return processed_text

if __name__ == '__main__':
	app.run(debug=True)
