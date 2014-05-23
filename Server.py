import tornado.ioloop
import tornado.web
import tornado.websocket
import game
import json
from time import sleep

#import pdb;pdb.set_trace()

clients = []

#stuurt message naar alle connected clients
def broadcast(message):
    for client in clients:
        client.write_message(message)


def send(client, message):
    client.write_message(message)


#
# def sendConnectedClientIPs(client):
#     print("send start")
#     clientNames = []
#     i = 0
#     while (i < clients.__len__()):
#         clientNames.append(clients[i].request.remote_ip)
#         i += 1
#     client.write_message(json.dumps(clientNames))
#     print("send end")

def handleMessage(originClient, message):
    splat = message.split(" ");
    if(splat[0] == "CREATEROOM"):
        newplayer = game.WebPlayer()
        newplayer.naam = splat[1]




#als een speler de server joint wordt hij geadd aan lijst van clients.
class JoinHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        print("someone connected")
        clients.append(self) # we appenden de client niet. we laten ze pas toevoegen als z


    def on_message(self, message):
        print("received" + message)
        handleMessage(self, message)


    def on_close(self):
        print("someone closed")
        clients.remove(self)


app = tornado.web.Application([(r'/', JoinHandler)])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()