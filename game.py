import random

import config as CFG
from dice import Dice
from tokens import Tokens
from station import Station

import create_sp_rooms
import create_rooms
import create_path
#import create_player1

class Game:

    def __init__(self, players_num: int) -> None:

        self.players_num = players_num

        self.station = Station()
        create_rooms.add_rooms(self.station)
        create_sp_rooms.add_sp_rooms(self.station)
        create_path.add_path(self.station)

        # Coordinates setup
        self.CRD = CFG.COORDINATES
        random.shuffle(self.CRD)
        self.coodinates = {
            "A": self.CRD[0],
            "B": self.CRD[1],
            "C": self.CRD[2],
            "D": self.CRD[3]
        }
        self.station.set_destination("B")

        # Escape pod setup
        if (self.players_num == 1) or (self.players_num == 2):
            self.pods = CFG.ESCAPE_POD_1_2
        elif (self.players_num == 3) or (self.players_num == 4):
            self.pods = CFG.ESCAPE_POD_3_4
        else:
            self.pods = CFG.ESCAPE_POD_5

        # Intruders tokens bag (pool) setup
        self.pool = Tokens(CFG.START_INTRUDERS_TOKENS)
        for _ in range(self.players_num):
            self.pool.add("ADULT")  # add ADULT per player

        # Init Noise and Combat dice
        self.noise_roll = Dice(CFG.NOISE_DIE)
        self.combat_roll = Dice(CFG.COMBAT_DIE)

        #self.intruders = []
        self.players = []

        #self.players.append(create_player1.create_player())
        #self.station.enter_room(self.players[0], "17")

        self.time_track = CFG.TIME_TRACK

    def get_station(self):
        return self.station

    def get_pool(self):
        return self.pool

    def get_noise_roll(self):
        return self.noise_roll
    
    def get_combat_roll(self):
        return self.combat_roll


    def add_player(self, player):

        if len(self.players) == 0:
            self.players.append(player)
            self.station.enter_room(player, CFG.START_ROOM)
            return True, "Added first player"
        
        else:
            description = player.description
            for each in self.players:
                if description["name"] == each.get_name() or \
                   description["color"] == each.get_color() or \
                   description["character"] == each.get_character():
                
                    return False, "Already exists"
                   
            self.players.append(player)
            self.station.enter_room(player, CFG.START_ROOM)
        
        return True, "Added new player"    


    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def get_user_player(self, user: str):
        for each in self.players:
            if user == each.get_name():
                return each
        return
    
    def get_player(self, num: int):
        '''
        Return Player object with number "num"
        '''
        return self.players[num - 1]  #FIXME


    def reset_game(self):

        for plr in self.players:
            self.players.remove(plr)

        self.__init__(CFG.PLAYERS)

        print("Reset..")


if __name__ == "__main__":

    game = Game(2)

    print(game.coodinates)

    print("Destination: ", game.station.check_destination())
    print("Pods: ", game.pods)

    for num in range(3):
        print(game.station.check_engine(num+1))

    game.get_pool().show()

    print("Noise: ", game.get_noise_roll().roll())
    print("Combat: ", game.get_combat_roll().roll())

    print("Time :", game.time_track)
