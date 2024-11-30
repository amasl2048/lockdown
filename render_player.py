from flask import render_template

from config import DEBUG

def render_player(user, game):

    station1 = game.get_station()
    player1 = game.get_user_player(user)

    if not player1:
        current_room = ""
        name = user
        character = ""
        stat = ""
        rooms_list = []

    else:
        current_room = player1.get_location()
        name = player1.get_name()
        character = player1.get_character()
        stat = player1.get_stat()
        rooms_list = station1.rooms[current_room].get_connected_rooms()
        
    connected_rooms = " ".join(rooms_list)

    # DEBUG
    description = ""
    state = ""
    if DEBUG:
        description = player1.description
        state = player1.state

    return render_template("player.html",
                            user=user,
                            name=name,
                            character= character,
                            stat=stat,
                            room=current_room,
                            connected_rooms=connected_rooms,
                            rooms_list=rooms_list,
                            description=description,
                            state=state,
                            error="")
