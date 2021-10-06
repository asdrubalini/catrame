from flask import Flask
from database import insert_reading

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "ciao"


@app.route("/insert", methods=["GET"])
def insert():
    insert_reading(1, 22.34)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
