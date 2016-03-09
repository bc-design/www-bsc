from flask import Flask, render_template, make_response, request
app = Flask(__name__)

import string
import sys
import traceback
import journal_lookup
from automaton import *

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

#@app.route('/automata/')
#def generate_automata():
#	# generates a simple cellular automaton
#	try:
#                img = imgCreate(18,200,400) 
#		response = make_response(img)
#        	response.headers["Content-Disposition"] = "inline; filename=cellular_automata_rule-018.bmp"#
#		response.headers["Content-Type"] = "image/bmp"
#        except:
#                print "Unexpected error:", sys.exc_info()[0] #testing
#                print traceback.format_exc() #testing
#	return response
#	#send_file(response,mimetype="image/bmp",as_attachment=True,attachment_filename="cellular_automata_rule-018.bmp") # for flask 0.9+ only!

@app.route('/automaton/', methods=['POST'])
def generate_automaton():
	try:
		ruleNum = int(request.form['ruleNum'])
		if ruleNum>=0 and ruleNum<=255:
                        img = imgCreate(int(ruleNum),200,400)
                        response = make_response(img)
                        response.headers["Content-Disposition"] = "inline; filename=cellular_automata_rule-"+str(ruleNum).zfill(3)+".bmp"
                        response.headers["Content-Type"] = "image/bmp"
		else:
			response = make_response('<br /><br /><button onclick=\"goBack()\">Number out of range!</button>'+'<script>function goBack() {window.history.back()}</script>') 
	except:
                print "Unexpected error:", sys.exc_info()[0] #testing
                print traceback.format_exc() #testing
		response = make_response('<br /><br /><button onclick=\"goBack()\">An error has occurred!</button>'+'<script>function goBack() {window.history.back()}</script>')
	return response

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
		response = make_response(string.join(results,"<br />")+'<br /><br /><button onclick=\"goBack()\">Look up more journals</button>'+'<script>function goBack() {window.history.back()}</script>')
	return response

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
