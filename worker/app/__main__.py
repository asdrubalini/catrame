import time
import requests
import random


def insert_reading(sensor_id: int, temperature: float):
    requests.post("http://api:8001/insert", json = {
        "sensor_id": sensor_id,
        "temperature": temperature
    })


if __name__ == "__main__":
    while True:
        insert_reading(random.randint(1, 4), random.uniform(20.0, 25.0))
        time.sleep(1)
