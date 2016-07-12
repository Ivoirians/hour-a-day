def websocket_app(environ, start_response):
    if environ["PATH_INFO"] == '/ws/echo':
        ws = environ["wsgi.websocket"]
        message = ws.receive()
        ws.send(message)