from rest_framework import serializers

from note_crud.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'hexColor', 'datetime')
