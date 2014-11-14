#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

print 'Content-Type: text/html'
print

if 'adjective1' not in form.keys():
	print ('<form action="madlibs.cgi">'
		'Enter an ADJECTIVE: <input type=text name=adjective1><br />'
		'Enter a NOUN: <input type=text name=noun1><br />'
	        'Enter a VERB: <input type=text name=verb1><br />'
        	'<input type=submit value="Alright!">')
else:
	adj1 = form.getvalue('adjective1','adjective')
	noun1 = form.getvalue('noun1','noun')
	verb1 = form.getvalue('verb1','verb')

	print adj1, noun1, verb1
