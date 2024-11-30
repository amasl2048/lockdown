from flask import render_template

from config import DEBUG, START_ROOM

def render_room(user, game, room, action, msg):

    station1 = game.get_station()

    if action:
        result = "Done."
        msg_color = "Green"
    else:
        result = "Action Failed."
        msg_color = "Tomato"

    if not room:
        room = START_ROOM

    explored, room_name = station1.rooms[room].check_room()
    rooms_list = station1.rooms[room].get_connected_rooms()
    connected_rooms = " ".join(rooms_list)
    effect = station1.rooms[room].effect()
    items = station1.rooms[room].items()

    if explored:
        players = station1.rooms[room].get_players_characters()
        intruders = station1.rooms[room].get_intruders_names()
        objects = ", ".join(station1.rooms[room].heavy_objects)
    else:
        players = "Unknown"
        intruders = "Unknown"
        objects = "Unknown"

    # DEBUG
    description = ""
    state = ""
    if DEBUG:
        description = station1.rooms[room].description
        state = station1.rooms[room].state

    return render_template("room.html",
                           user=user, 
                           room=room,
                           room_name=room_name,
                           effect=effect,
                           items=items,
                           description=description,
                           connected_rooms=connected_rooms,
                           state=state,
                           players=players,
                           intruders=intruders,
                           objects=objects,
                           result=result,
                           msg_color=msg_color,
                           rooms_list=rooms_list,
                           error=msg)
