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
from api.counter import Counter

def start(environ, start_response):
	request = Request(environ)
	test = "Service not found."
	service = request.path.split("svc")[1]
	if service == '/rollDie':	
		test = random.randint(1, 6)
	if service == '/counter/get':
		test = Counter.getCounterValue()
	if service == '/counter/add':
		test = Counter.addCounterValue()
	response = Response(str(test), mimetype='text/plain')
	return response(environ, start_response)

