from django.db.models.aggregates import Avg
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from .models import Reading, Sensor

MAX_READINGS_COUNT = 128


@csrf_exempt
def reading(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse("POST only")

    if "sensor_id" not in request.POST or "temperature" not in request.POST:
        return HttpResponse("Missing sensor_id or temperature", status=400)

    sensor_id = request.POST["sensor_id"]
    temperature = request.POST["temperature"]

    print("Inserting: ", sensor_id, temperature, flush=True)

    # Get or create sensor
    sensor = Sensor.objects.get_or_create(sensor_id=sensor_id)[0]
    # Insert reading
    Reading.objects.create(sensor=sensor, temperature=temperature)

    return HttpResponse("ok")


def readings(request: HttpRequest):
    if request.method != "GET":
        return HttpResponse("GET only")

    readings_count = Reading.objects.count()
    readings = Reading.objects.all().order_by("-id")[:MAX_READINGS_COUNT]
    average = round(Reading.objects.all().aggregate(Avg("temperature"))["temperature__avg"], 2)

    html = f"<pre>There are {readings_count} readings, showing the last {MAX_READINGS_COUNT}</pre>"
    html += f"<pre>The average temperature is {average} C</pre>"

    for reading in readings:
        html += "<pre>"
        html += str(reading)
        html += "</pre>"

    return HttpResponse(html)
