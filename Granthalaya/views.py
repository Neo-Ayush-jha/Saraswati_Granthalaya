from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class BookView(APIView):
    book=Book.objects.all()
    serializer = BookSerializer(book,many=True)
    def get(self,req):
        # return Response(self.serializer.data,status=200)
        return Response(self.serializer.data, status=status.HTTP_200_OK)
    def post(self,req):
        serializer = BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data,status=200)
            return Response(self.serializer.data, status=status.HTTP_200_OK)