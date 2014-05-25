__author__ = 'Drareeg'
import json
import logging


class Room:  #hehe he
    players = list()
    id = int


    def __init__(self, id):
        logging.info("room made")
        self.id = id


    def join(self, player):
        logging.info("%s tries joining room" % player.name)
        self.players.append(player)
        return 1  #if succes, currently always accepting players


    def to_json(self):
        return json.dumps(self.id) + "," + json.dumps(self.players.__len__())


class WebPlayer:
    def __init__(self, name):
        self.name = name


    def to_json(self):
        return self.name



logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)