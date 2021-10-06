from flask import Flask, request
from flask.wrappers import Response
from database import insert_reading, fetch_readings

import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    readings = fetch_readings()

    html = ""
    for reading in readings:
        html += f"<pre>{reading}</pre>"
    
    return html


@app.route("/insert", methods=["POST", "GET"])
def insert_reading():
    data = request.json

    if not data or ("sensor_id" not in data or "temperature" not in data):
        return Response("Missing required parameters", status=400)

    sensor_id = data["sensor_id"]
    temperature = data["temperature"]

    insert_reading(sensor_id, temperature)

    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
