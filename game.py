__author__ = 'Drareeg'
import logging
import random


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# the abstract object representing the game
class Game:
    def __init__(self):
        self.players = ()
        self.started = False
        self.turns = 10
        self.current_turn = 0

    def join_game(self, player):
        if not self.started:
            self.players.append(player)
            player.set_game(self)
        else:
            raise Exception("Cant join a started game")

    def deal(self):
        self.started = True
        deck = Deck()
        for i in range(self.turns):
            for player in self.players:
                player.add_card(deck.get_next_card())

    def check_all_players_selected(self):
        for player in self.players:
            if player.selected_card is None:
                return False
        return True




class Player:
    def __init__(self, name):
        self.name = name
        self.cards = ()
        self.selected_card = None
        self.game = None

    def add_card(self, card):
        self.cards.append(card)

    def to_json(self):
        return self.name

    def set_game(self, game):
        self.game = game

    #the x-th card in hand
    def select_card(self, card):
        if card < len(self.cards):
            self.selected_card = self.cards(i)


class Card:
    def __init__(self, value, points):
        self.value = value
        self.points = points


class Deck:
    def __init__(self):
        self.cards = ()
        for i in range(104):
            self.cards.append(Card(i, 1))

        random.shuffle(self.cards)


    def get_next_card(self):
        return self.cards.pop()





