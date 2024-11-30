#!/bin/env python3
from os import path
from flask import Flask
from flask import request
from flask_httpauth import HTTPDigestAuth

from start_game import game1
from action_move import move
from action_melee_attack import melee_attack

from create_player import create_player

from render_room import render_room
from render_player import render_player
from render_station import render_station
from render_settings import render_settings

from users import USERS

APP_PORT = 8888

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = path.join('static')
app.config['SECRET_KEY'] = 'qwDJ_125'
auth = HTTPDigestAuth()

@auth.get_password
def get_pw(username):
    if username in USERS:
        return USERS.get(username)
    return None

@app.route('/', methods=['GET'])
@auth.login_required
def root():
    user = auth.username()
    return render_settings(user, "", "")


@app.route('/player', methods=['GET'])
@auth.login_required
def player():
    user = auth.username()
    return render_player(user, game1)


@app.route('/move', methods=['POST'])
@auth.login_required
def action_move():

    user = auth.username()
    room = request.form.get("room")
    res, msg = move(game1.get_station(), game1.get_user_player(user), room)

    return render_room(user, game1, room, res, msg)

@app.route('/melee_attack', methods=['POST'])
@auth.login_required
def action_melee_attack():

    user = auth.username()
    room = request.form.get("room")
    alien = request.form.get("alien")
    res, msg = melee_attack(game1, user, alien)

    return render_room(user, game1, room, res, msg)

@app.route('/room', methods=['GET'])
@auth.login_required
def room():

    user = auth.username()
    room = request.args.get("room")

    return render_room(user, game1, room, True, "")


@app.route('/rooms', methods=['GET'])
@auth.login_required
def rooms():

    user = auth.username()
    return render_rooms()  #FIXME: not used

@app.route('/settings', methods=['GET'])
@auth.login_required
def settings():

    user = auth.username()
    return render_settings(user, "", "")

@app.route('/reset', methods=['POST'])
@auth.login_required
def reset():

    user = auth.username()
    game1.reset_game()

    return render_settings(user, "", "")

@app.route('/create_player', methods=['POST'])
@auth.login_required
def person():

    user = auth.username()
    name = user
    color = request.form.get("color")
    character = request.form.get("character")

    player = create_player(name, color, character)
    res, msg = game1.add_player(player)
    if res:
        msg_color = "DarkGreen"
    else:
        msg_color = "Tomato"

    return render_settings(user, msg, msg_color)

@app.route('/station', methods=['GET'])
@auth.login_required
def station_rooms():

    user = auth.username()
    map_png = path.join(app.config['IMAGE_FOLDER'], 'map.png')

    return render_station(user, game1, map_png)


if __name__ == "__main__":

    app.run(debug = True, host = "0.0.0.0", port = APP_PORT)
