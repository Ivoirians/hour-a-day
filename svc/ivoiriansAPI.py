import os
import redis
import code
import urlparse
import json
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
import random
from api.counter import Counter
from api.comments import Comments

def rollDie(request):
	return random.randint(1,6)

def getCounter(request):
	return Counter.getCounterValue()

def addCounter(request):
	return Counter.addCounterValue()

def getComments(request):
	qs = urlparse.parse_qs(request.query_string)
	return Comments.getComments(qs["page_number"])

def addComment(request):
	formData = json.loads(request.data)
	return Comments.addComment(formData["page_number"], formData["username"], formData["comment_text"])

services = {
	'/rollDie': rollDie,
	'/counter/get': getCounter,
	'/counter/add': addCounter,
	'/comments/get': getComments,
	'/comments/add': addComment,
}

def start(environ, start_response):
	request = Request(environ)

	responseBody = "Service not found."

	try:
		responseBody = services[request.path.split("svc")[1]](request)
	except Exception as e:
		responseBody = "Could not execute service " + request.path.split("svc")[1] + ": \n" + str(e)

	response = Response(str(responseBody), mimetype='text/plain')
	return response(environ, start_response)

