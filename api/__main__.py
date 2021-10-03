from flask import Flask

import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
    host="database",
    port=3306,
    user="giovanni",
    password="catrame",
    database="giovanni"
)


@app.route("/")
def index():
    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT * FROM `sensors`")

    # Fetch one result
    rows = cur.fetchall()

    return str(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
