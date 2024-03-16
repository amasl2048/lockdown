from flask import render_template

from config import DEBUG

def render_room(game, room, action, msg):

    station1 = game.get_station()

    if action:
        result = "Done."
        msg_color = "Green"
    else:
        result = "Action Failed."
        msg_color = "Tomato"

    explored, room_name = station1.rooms[room].check_room()
    rooms_list = station1.rooms[room].get_connected_rooms()
    connected_rooms = " ".join(rooms_list)
    effect = station1.rooms[room].effect()
    items = station1.rooms[room].items()

    if explored:
        players = station1.rooms[room].get_players_names()
        intruders = station1.rooms[room].get_intruders_names()
    else:
        players = "Unknown"
        intruders = "Unknown"

    # DEBUG
    description = ""
    state = ""
    if DEBUG:
        description = station1.rooms[room].description
        state = station1.rooms[room].state

    return render_template("room.html", 
                           room=room,
                           room_name=room_name,
                           effect=effect,
                           items=items,
                           description=description,
                           connected_rooms=connected_rooms,
                           state=state,
                           players=players,
                           intruders=intruders,
                           result=result,
                           msg_color=msg_color,
                           rooms_list=rooms_list,
                           error=msg)
