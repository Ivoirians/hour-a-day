def websocket_app(environ, start_response):
    print environ
    if environ["PATH_INFO"] == '/ws/echo':
        ws = environ["wsgi.websocket"]
        message = ws.receive()
	print message
        ws.send(message)
