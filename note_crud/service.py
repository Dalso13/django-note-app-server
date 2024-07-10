from abc import ABC, abstractmethod

from note_crud.models import Note
from note_crud.serializer import NoteSerializer


class NoteService(ABC):
    @abstractmethod
    def create(self, title, content, hexColor):
        pass


    @abstractmethod
    def readAll(self):
        pass

    @abstractmethod
    def update(self, id, title, content, hexColor):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class NoteServiceEx(NoteService):

    def create(self, title: str, content: str, hexColor: int):
        Note.objects.create(
            title=title,
            content=content,
            hexColor=hexColor,
        )

    def readAll(self):
        try:
            return NoteSerializer(Note.objects.all(), many=True).data
        except Exception as e:
            print(e)
            return False

    def update(self, id, title, content, hexColor):
        try:
            model = Note.objects.filter(id=id)
            data = model.update(title=title, content=content, hexColor=hexColor)
            print(data)
        except Exception as e:
            print(e)
            return False

    def delete(self, id):
        try:
            model = Note.objects.filter(id=id)
            data = model.delete()
            print(data)
        except Exception as e:
            print(e)
            return False
