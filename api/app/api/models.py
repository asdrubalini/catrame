from django.db import models


class Sensor(models.Model):
    sensor_id = models.IntegerField()
    sensor_name = models.TextField(default="Nessun nome", unique=False)

    def __str__(self):
        return f"Sensor(sensor_id={self.sensor_id}, sensor_name={self.sensor_name})"


class Reading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    temperature = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reading(sensor={self.sensor}, temperature={round(self.temperature, 2)}, created_at={self.created_at})"
