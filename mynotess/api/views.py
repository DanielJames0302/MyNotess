from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import updateNote, getNoteDetail
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]


    return Response(routes)




@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        note = Note.objects.all().order_by('-updated')
        serializer = NoteSerializer(note, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        note = Note.objects.create(
            body = data['body']
        )
        serializer = NoteSerializer(note, many = False)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
       return getNoteDetail(request, pk)
    if request.method == 'PUT':
       return updateNote(request,pk)
    
    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('Note was deleted!')
    





