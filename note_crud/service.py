from abc import ABC, abstractmethod

from note_crud.models import Note
from note_crud.serializer import NoteSerializer


class NoteService(ABC):
    @abstractmethod
    def create(self, title, content, hexColor):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, id, title, content, hexColor):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class NoteServiceEx(NoteService):
    def __init__(self):
        self.note = Note()

    def create(self, title: str, content: str, hexColor: int):
        self.note.objects.create(
            title=title,
            content=content,
            hexColor=hexColor,
        )

    def read(self, id: int):
        return NoteSerializer(self.note.objects.get(id=id)).data

    def update(self, id, title, content, hexColor):
        self.note.objects.filter(id=id).update(title=title, content=content, hexColor=hexColor)

    def delete(self, id):
        return self.note.objects.filter(id=id).delete()
