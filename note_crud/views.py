import json

from django.http import HttpResponse, HttpRequest
from note_crud.service import NoteServiceEx
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
service = NoteServiceEx()


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello world")


@csrf_exempt
def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        body = json.loads(request.body)
        title = body.get('title')
        content = body.get('content')
        hexColor = body.get('hexColor')

        if not title and not hexColor and not content:
            return HttpResponse(status=400)
        service.create(title, content, hexColor)
        return HttpResponse(status=200)


def readAll(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse(json.dumps(service.readAll())
                            , content_type="text/json-comment-filtered",
                            status=200, )


@csrf_exempt
def update(request: HttpRequest) -> HttpResponse:
    if request.method == 'PUT':
        id = request.PUT.get('id')
        title = request.PUT.get('title')
        content = request.PUT.get('content')
        hexColor = request.PUT.get('hexColor')

        if not id and not title and not hexColor and not content:
            return HttpResponse(status=400)

        service.update(title, content, hexColor)
        return HttpResponse(status=200)


@csrf_exempt
def delete(request: HttpRequest) -> HttpResponse:
    if request.method == 'DELETE':
        id = request.DELETE.get('id')
        if not id:
            return HttpResponse(status=400)
        service.delete(id)
        return HttpResponse(status=200)
