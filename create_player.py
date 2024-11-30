from config import START_ROOM
from person import Person

def create_player(name, color, character):

    player = Person(name=name,
                    color=color,
                    character=character,
                    room_id=START_ROOM
                    )

    return player
