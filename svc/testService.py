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
import sqlite3

def getCounterValue():
	conn = sqlite3.connect('ivoirians.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM tb_Counter")
	ret = cur.fetchone()[0]	
	conn.close()	
	return ret

def addCounterValue():
	conn = sqlite3.connect('ivoirians.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM tb_Counter")
	prev = cur.fetchone()[0]
	cur.execute("UPDATE tb_Counter SET intCounterValue=?", (int(prev) + 1,))
	conn.commit()
	conn.close()
	return int(prev) + 1

def application(environ, start_response):
	request = Request(environ)
	test = "Service not found."
	if request.path == '/svc/rollDie':	
		test = random.randint(1, 6)
	if request.path == '/svc/counter/get':
		test = getCounterValue()
	if request.path == '/svc/counter/add':
		test = addCounterValue()
	response = Response(str(test), mimetype='text/plain')
	return response(environ, start_response)

