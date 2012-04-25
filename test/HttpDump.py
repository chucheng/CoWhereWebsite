from __future__ import print_function
import httplib


def _read_loop(resp):
    while True:
        if resp.isclosed():
            print("disconnected")
            break
        try:
            c = resp.read(1)
            print(c, end='')            
        except httplib.IncompleteRead as e:
            print("error:" + str(e))
        

if __name__ == "__main__":  
    
    conn = httplib.HTTPConnection("localhost", "8888")
    conn.request('GET', "http://localhost:8888/recv/", "", {})
    resp = conn.getresponse()
    
    if resp.status == 200:
        print("get http 200 ok")
    print("-----")
    
    _read_loop(resp)
