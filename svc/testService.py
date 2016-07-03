import os
import redis
import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
import random


def application(environ, start_response):
	request = Request(environ)
	test = ''
	if request.path == '/svc/rollDie':	
		test = str(random.randint(1, 6))
	response = Response(test, mimetype='text/plain')
	return response(environ, start_response)

