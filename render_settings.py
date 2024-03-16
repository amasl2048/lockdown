from flask import render_template

from config import DEBUG

def render_settings(msg, msg_color):

    return render_template("settings.html", msg=msg, msg_color=msg_color)
