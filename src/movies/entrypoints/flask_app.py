from flask import Flask, request
from movies import models

app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/", methods=["GET"])
def display_recommendations():
    hello_world()