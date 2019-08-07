from django.http import HttpResponse
from .models import Notes
from .serializers import NotesSerializer

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


import json
'''
    Technical test for PLAYVOX
    Author: Mario Fernando Espinosa
    API REST Framework Notes
    August 01 2019
'''

#API NOTES
class NotesView(APIView):

    #Get all notes from a specific user
    def get(self, request, iduser):
        print(iduser)
        notes = Notes.objects.filter(iduser=iduser)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create a new Note
    def post(self, request, format=None):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
