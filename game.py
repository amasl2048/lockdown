import config as CFG
from dice import Dice
from tokens import Tokens
from station import Station

import create_sp_rooms
import create_rooms
import create_path
import create_player1

class Game:

    def __init__(self) -> None:

        self.station = Station()
        create_rooms.add_rooms(self.station)
        create_sp_rooms.add_sp_rooms(self.station)
        create_path.add_path(self.station)

        self.pool = Tokens(CFG.INTRUDERS_TOKENS)

        self.noise_roll = Dice(CFG.NOISE_DICE)

        self.intruders = []
        self.players = []

        self.players.append(create_player1.create_player())
        self.station.enter_room(self.players[0], "17")

    def get_station(self):
        return self.station

    def get_pool(self):
        return self.pool

    def get_noise_roll(self):
        return self.noise_roll

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def get_player(self):
        return self.players[0]  #FIXME


    def reset_game(self):

        for plr in self.players:
            self.players.remove(plr)

        self.__init__()

        print("Reset..")
