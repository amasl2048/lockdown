from flask import render_template

from config import DEBUG

def render_settings(user, msg, msg_color):

    return render_template("settings.html", 
                           user=user,
                           msg=msg,
                           msg_color=msg_color)
