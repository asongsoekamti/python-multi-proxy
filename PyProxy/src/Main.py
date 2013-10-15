#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2013-09-29

@author: DeadSakura
'''
import SocketServer,httplib

class MyTCPHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        self.data = self.rfile
        print "{}:{} wrote:".format(self.client_address[0],self.client_address[1])
        #print "{} {} wrote:".format(self.)
        for line in self.data:
            if (line == "\r\n"):
                print "Hit end."
                print "Data received: " + str(self.data.__sizeof__())
                break
            else:
                print line[:-2]
        conn = httplib.HTTPConnection("www.google.com")
        conn.request("GET", "/")
        readData = conn.getresponse()
        print readData
        self.wfile.write(readData)

if __name__ == '__main__':
    print "正在启动PMP……"
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    