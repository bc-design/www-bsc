#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www2/www-bsc/flask/")

from FlaskApp import app as application
# application.secret_key = 'Add your secret key'
