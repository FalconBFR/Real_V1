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

while True:
    name_input = input("What do you want to add (name)")
    if name_input ==".":
        server.close()
        break
    x_input = input("What do you want to add (x)")
    y_input = input("What do you want to add (y)")
    z_input = input("What do you want to add (z)")
    for client in clients:
    #client.sendMessage(unicode(json.dumps({'x': x / w, 'y': y / h, 'radius': radius / w})))
        client.sendMessage(str(json.dumps({'obj_name':name_input,'x': x_input, 'y':y_input, 'z':z_input})))






server.close()
