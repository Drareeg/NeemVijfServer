import tornado.ioloop
import tornado.web
import tornado.websocket
import game
import json
import Encoder
import random
import logging
#import pdb;pdb.set_trace()

clients = []
rooms = {}

#stuurt message naar alle connected clients
def broadcast(message):
    for client in clients:
        client.write_message(message)


def send(client, message):
    client.write_message(message)


def handlemessage(originclient, message):
    splat = message.split(" ");
    if splat[0] == "CREATEROOM":
        room = game.Room(random.randint(1, 1))  #logica achter het gekozen id steken
        rooms[room.id] = room
    if splat[0] == "GETROOMS":
        send(originclient, json.dumps(rooms, cls=Encoder.CustomEncoder, indent=2))
    if splat[0] == "JOINROOM":  #JOINROOM roomid playername
        room = rooms.get(int(splat[1]))  #handle null
        if room.join(game.WebPlayer(splat[2])):
            send(originclient, "you joined room ")


class MessageHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        logging.info("someone connected")
        clients.append(self)


    def on_message(self, message):
        logging.info("received " + message)
        handlemessage(self, message)


    def on_close(self):
        logging.info("someone closed")
        clients.remove(self)


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
app = tornado.web.Application([(r'/', MessageHandler)])

app.listen(8889)
tornado.ioloop.IOLoop.instance().start()


