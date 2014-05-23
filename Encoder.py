__author__ = 'Drareeg'
import game
import json


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        print(obj)
        if isinstance(obj, game.Room):
            print("is room")
            return obj.to_json()

        return json.JSONEncoder.default(self, obj)
