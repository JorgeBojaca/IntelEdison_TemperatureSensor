import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import temperature_sensor2
import time

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        while True:
            time.sleep(1)
            temp = temperature_sensor2.getTemperature()
            self.write_message(temp)
                  
    def on_message(self, message):
        print 'message received %s' % message
 
    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/currentTemperature', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    #myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started ***'
    tornado.ioloop.IOLoop.instance().start()
