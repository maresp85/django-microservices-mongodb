from django.http import HttpResponse
from .models import Users
from .serializers import UsersSerializer

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

import json
'''
    Technical test for PLAYVOX
    Author: Mario Fernando Espinosa
    API REST Framework
    August 01 2019
'''

#Pagination
class Pagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        })

#get all Users with Pagination
class UserList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    pagination_class = Pagination

#API USER CRUD
class UsersView(APIView):

    #Get all records from Users
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create a new User
    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            #check if user exists (email)
            try:
                users = Users.objects.get(email=request.data['email'])
                return Response('user exists', status=status.HTTP_400_BAD_REQUEST)
            except Users.DoesNotExist:
                serializer.save()
                users = Users.objects.all()
                serializer = UsersSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Update User
    def put(self, request, pk, format=None):
        users = Users.objects.get(pk=pk)
        serializer = UsersSerializer(users, data=request.data)
        if serializer.is_valid():
            # check if user exists (email)
            try:
                users = Users.objects.get(email=request.data['email'])
                return Response('user exists', status=status.HTTP_400_BAD_REQUEST)
            except Users.DoesNotExist:
                serializer.save()
                users = Users.objects.all()
                serializer = UsersSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete User
    def delete(self, request, pk, format=None):
        try:
            users = Users.objects.get(pk=pk)
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("error delete", status=status.HTTP_400_BAD_REQUEST)

#API Search
class UsersSearch(APIView):

    # Search User by First Name
    def get(self, request):
        users = Users.objects.filter(first_name__icontains=request.GET['query'])
        serializer = UsersSerializer(users, many=True)
        #return Response("ok")
        return Response(serializer.data, status=status.HTTP_200_OK)
