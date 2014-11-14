#!/usr/bin/env python

import random
import cgi

form = cgi.FieldStorage()
sentences=[
	('VERB','ADJECTIVE','NOUN','Do not ',' the ',' ','!'),
	('VERB','ADJECTIVE','NOUN','I hate to ',' the ',' ','!'),
	('NOUN','VERB','NOUN','','s should not ',' the ','!'),
	('ADJECTIVE','NOUN','NOUN','It is a little-known fact that ',' ','s love ','s!'),
	('ADJECTIVE','NOUN','ADJECTIVE','My ',' ', ' ate my ', ' homework!')
	]

print 'Content-Type: text/html'
print
print '<h1>Mad Libs</h1>'

if len(form.keys())==0:
	random.seed()
	sent = random.randint(0,len(sentences)-1)

	print '<form action="madlibs.cgi">'
	print '<input type="hidden" name="sent" value="' + str(sent) + '">'
	print 'Enter a ' + str(sentences[sent][0]) + ': <input type=text name=input1><br />'
	print 'Enter a ' + str(sentences[sent][1]) + ': <input type=text name=input2><br />'
	print 'Enter a ' + str(sentences[sent][2]) + ': <input type=text name=input3><br />'
        print '<input type=submit value="Alright!">'

else:
	sent = int(form.getvalue('sent'))
	input1 = form.getvalue('input1',sentences[sent][0])
	input2 = form.getvalue('input2',sentences[sent][1])
	input3 = form.getvalue('input3',sentences[sent][2])

	print sentences[sent][3] + input1 + sentences[sent][4] + input2 + sentences[sent][5] + input3 + sentences[sent][6]
	print '<br /><br />'
	print ('<form action="http://www.brandoncurtis.com/cgi/madlibs.cgi">'
		'<input type="submit" value="Try another one!">'
		'</form>')
