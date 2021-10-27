from django.http import HttpResponse, HttpRequest


def reading(request: HttpRequest):
    if request.method == "GET":
        return HttpResponse("Hello, world. You're at the polls index.")

    elif request.method == "POST":
        # Insert model
        pass
