# a flask server that uses pyautogui to send right arrow and left arrow commands
from flask import Flask, request
from pyautogui import press
import time

app = Flask(__name__)


@app.route("/right")
def right():
    press("right")
    return "right"


@app.route("/left")
def left():
    press("left")
    return "left"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
