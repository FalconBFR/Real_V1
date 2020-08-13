import cv2
import numpy as np
import threading
import json
import time
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


server = None
clients = []


class SimpleWSServer(WebSocket):
    def handleConnected(self):
        clients.append(self)

    def handleClose(self):
        clients.remove(self)


def run_server():
    global server
    server = SimpleWebSocketServer('', 9000, SimpleWSServer,
                                   selectInterval=(1000.0 / 15) / 1000)
    server.serveforever()


t = threading.Thread(target=run_server)
t.start()

var = 0 #self set
while True:
    for client in clients:
    #client.sendMessage(unicode(json.dumps({'x': x / w, 'y': y / h, 'radius': radius / w})))
        var+=0.1
        client.sendMessage(str(json.dumps({'x': var, 'y':var, 'z':var})))
    a_input = input("break command")
    if a_input ==".":
        server.close()
        break




server.close()
