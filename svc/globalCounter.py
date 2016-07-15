from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
import json

class CounterApplication(WebSocketApplication):
    def on_open(self):
        print "Client connected."

    def on_message(self, message):
        if message is None:
	   return
        message = json.loads(message)

        if message['message_type'] == 'increment':
            self.broadcast(message)

    def broadcast(self, message):
        for client in self.ws.handler.server.clients.values():
            client.ws.send(json.dumps({
                'message_type': 'increment_notification'
		}))

    def on_close(self, reason):
        print "Client disconnected."

WebSocketServer(
    ('0.0.0.0', 8002),
    Resource({'/ws/counter': CounterApplication}),
    debug=False
).serve_forever() 
