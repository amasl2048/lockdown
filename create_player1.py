from person import Person

def create_player():

    current_room = "17"
    player1 = Person(name="Andrew",
                    color="Blue",
                    character="HACKER",
                    room_id=current_room,
                    knowledge=1
                    )

    return player1
