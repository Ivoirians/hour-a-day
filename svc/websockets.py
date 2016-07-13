from geventwebsocket import WebSocketError

def websocket_app(environ, start_response):
    if environ["PATH_INFO"] == '/ws/echo':	        
	ws = environ["wsgi.websocket"]
	while True:
	    try:
                message = ws.receive()
                print message
	        ws.send(message)
            except WebSocketError:
                break
