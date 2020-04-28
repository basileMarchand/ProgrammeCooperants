from tornado import websocket, web, ioloop
import json


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def on_message(self, message):
        self.write_message(u"You said: " + message) 


app = web.Application([
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(3060)
    ioloop.IOLoop.instance().start()
