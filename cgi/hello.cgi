#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

x = int(form.getvalue('number','0'))     # Values are strings, so we need to convert.

print 'Content-Type: text/html'
print 
print '<h1>Hello!</h1>'
print 'The square of', x, 'is', x*x, '.'
