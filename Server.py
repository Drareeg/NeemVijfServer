import tornado.ioloop
import tornado.web
import tornado.websocket
import game
import json
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
        room = Room(random.randint(1, 1))  #logica achter het gekozen id steken
        rooms[room.roomId] = room
    if splat[0] == "GETROOMS":
        send(originclient, json.dumps(rooms, cls=MyEncoder, indent=2))
    if splat[0] == "JOINROOM":  #JOINROOM roomid playername
        room = rooms.get(int(splat[1]))  #handle null
        if room.join(game.Player(splat[2])):
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


class Room:  #hehe he



    def __init__(self, id):
        logging.info("room made")
        self.roomId = id
        self.players = list()


    def join(self, player):
        logging.info("%s tries joining room" % player.name)
        self.players.append(player)
        return 1  #if succes, currently always accepting players


    def to_json(self):
        return json.dumps(self.roomId) + "," + json.dumps(self.players.__len__())


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        print(obj)
        if isinstance(obj, Room):
            return obj.to_json()

        return json.JSONEncoder.default(self, obj)


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
app = tornado.web.Application([(r'/', MessageHandler)])

app.listen(8889)
tornado.ioloop.IOLoop.instance().start()


