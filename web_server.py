#!/bin/env python3
from os import path
from flask import Flask
from flask import request

from start_game import game1
from action_move import move

from render_room import render_room
from render_player import render_player
from render_station import render_station
from render_settings import render_settings

APP_PORT = 8002

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = path.join('static')

@app.route('/', methods=['GET'])
def root():

    map_png = path.join(app.config['IMAGE_FOLDER'], 'map.png')

    return render_station(game1, map_png)


@app.route('/player', methods=['GET'])
def player():
    return render_player(game1)


@app.route('/move', methods=['POST'])
def action_move():

    room = request.form.get("room")
    res, msg = move(game1.get_station(), game1.get_player(), room)

    return render_room(game1, room, res, msg)


@app.route('/room', methods=['GET'])
def room():

    room = request.args.get("room")

    return render_room(game1, room, True, "")


@app.route('/rooms', methods=['GET'])
def rooms():

    return render_rooms()

@app.route('/settings', methods=['GET'])
def settings():

    return render_settings("", "")

@app.route('/reset', methods=['POST'])
def reset():

    game1.reset_game()

    return render_settings("", "")

@app.route('/person', methods=['POST'])
def person():

    name = request.form.get("name")
    color = request.form.get("color")
    character = request.form.get("character")

    player1 = game1.get_player()
    res = player1.set_person(name, color, character)
    if res:
        msg = "Done."
        msg_color = "DarkGreen"
    else:
        msg = "Setting failed"
        msg_color = "Tomato"

    return render_settings(msg, msg_color)

@app.route('/station', methods=['GET'])
def station_rooms():

    map_png = path.join(app.config['IMAGE_FOLDER'], 'map.png')

    return render_station(game1, map_png)


if __name__ == "__main__":

    app.run(debug = False, host = "0.0.0.0", port = APP_PORT)
