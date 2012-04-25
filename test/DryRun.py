# DryRun Server -- nothing but broadcasting
#

import logging
import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):    
    pass



class ClientPool(object):
    client_callbacks = set()
    
    def join(self, callback):
        cls = ClientPool
        cls.client_callbacks.add(callback)
        
    def leave(self, callback):
        cls = ClientPool
        callback(messages="", close_resp=True)
        cls.client_callbacks.remove(callback)
        
    def broadcast(self, messages):
        cls = ClientPool
        for callback in cls.client_callbacks:
            try:
                callback(messages)
            except:
                logging.error("Error in client callback", exc_info=True)
                
    def shutdown_all_clients(self):
        cls = ClientPool
        for callback in cls.client_callbacks:
            callback(messages="", close_resp=True)
        cls.client_callbacks = set() #remove all call backs  

class RecieverHandler(BaseHandler, ClientPool):
    @tornado.web.asynchronous
    def get(self):
        self.join(self.on_new_messages)
        
    def on_new_messages(self, messages, close_resp=False):
        # connection is closed
        if self.request.connection.stream.closed():
            return
        self.write(messages)
        self.flush()
        if close_resp:
            self.finish()        
    
    #called when client closed the connection
    def on_connection_close(self):
        self.leave(self.on_new_messages)        
        pass    
        
class SenderHandler(BaseHandler, ClientPool):
    def get(self):
        cmd = self.get_argument("command")
        self.write("broadcasting..." + cmd)
        self.broadcast(cmd)
        self.write("...done")
        if cmd == "die":
            self.shutdown_all_clients()


application = tornado.web.Application([
    (r"/", HelloHandler),
    (r"/send/", SenderHandler),
    (r"/recv/", RecieverHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
