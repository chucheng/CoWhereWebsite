import time
import urlparse
import BaseHTTPServer

HOST_NAME = "localhost"
PORT_NUMBER = 81

class MirrorHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    Queue = "1234567" 
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
    def do_GET(self):        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()        
        
        query_str = urlparse.urlparse(self.path).query
        qs_dict = urlparse.parse_qs(query_str)
        self.log("Http GET: " + str(qs_dict))
        
        self.wfile.write("Mirror: " + query_str)        
        while(MirrorHandler.Queue):
            self.log(MirrorHandler.Queue)            
            time.sleep(1)
            MirrorHandler.Queue = MirrorHandler.Queue[1:]
            

            
    def log(self, message):
        print message
    
        

if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MirrorHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)