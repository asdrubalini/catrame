import time
import requests
import random
from dataclasses import dataclass

API_ENDPOINT = "http://api:8000"


@dataclass
class Reading:
    sensor_id: int
    temperature: float


def get_random_reading() -> Reading:
    return Reading(
        sensor_id=random.randint(1, 4), temperature=random.uniform(20.0, 25.0)
    )


def insert_reading(reading: Reading):
    requests.post(
        f"{API_ENDPOINT}/api/sensor",
        json={"sensor_id": reading.sensor_id, "temperature": reading.temperature},
    )


if __name__ == "__main__":
    while True:
        reading = get_random_reading()
        print(f"Inserting new reading: {reading}")

        insert_reading(reading)
        time.sleep(1)
