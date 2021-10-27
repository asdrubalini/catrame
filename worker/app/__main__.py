import time
import requests
import random
from dataclasses import dataclass
import threading

API_ENDPOINT = "http://api:8000"

SENSOR_COUNT = 256
RAND_SLEEP_MIN = 0.5
RAND_SLEEP_MAX = 2


@dataclass
class Reading:
    sensor_id: int
    temperature: float


def get_random_reading(sensor_id: int) -> Reading:
    return Reading(sensor_id=sensor_id, temperature=random.uniform(20.0, 25.0))


def insert_reading(reading: Reading):
    requests.post(
        f"{API_ENDPOINT}/api/reading",
        data={"sensor_id": reading.sensor_id, "temperature": reading.temperature},
    )


class SensorThread(threading.Thread):
    def __init__(self, sensor_id: int) -> None:
        super().__init__()

        self.sensor_id = sensor_id

    def __random_sleep(self):
        time.sleep(random.uniform(RAND_SLEEP_MIN, RAND_SLEEP_MAX))

    def run(self):
        while True:
            self.__random_sleep()

            reading = get_random_reading(self.sensor_id)
            print(
                f"[Sensor: {self.sensor_id}] Inserting new reading: {reading}",
                flush=True,
            )

            insert_reading(reading)


if __name__ == "__main__":
    for i in range(0, SENSOR_COUNT):
        SensorThread(sensor_id=i).start()

    # Sleep forever
    while True:
        time.sleep(1)
