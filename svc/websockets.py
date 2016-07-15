import gevent
from gevent.pywsgi import WSGIServer
from gevent.lock import Semaphore
from geventwebsocket.handler import WebSocketHandler, WebSocketError
from datetime import datetime

def websocket_app(environ, start_response):
    if environ["PATH_INFO"] == '/ws/echo':	        
	ws = environ["wsgi.websocket"]
	print ws
	print ""
	print ws.handler
	print ""
	print ws.handler.server
	print ""
	print ws.handler.server.clients
	print ""
	print ws.handler.server.clients.values()
	while True:
	    try:
                message = ws.receive()
                print message
	        ws.send(message)
            except WebSocketError:
                break

