from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def success_response(message,data=[]):
    response_data = {'data':data,'status': 'success', 'message': message}
    return Response(response_data, status=status.HTTP_200_OK)

def error_response(message, status_code):
    response_data = {'status': 'error', 'message': message}
    return Response(response_data, status=status_code)

class BookView(APIView):
    book=Book.objects.all()
    serializer = BookSerializer(book,many=True)
    def get(self,req):
        return success_response(data=self.serializer.data,message='Data added successfully.')
    def post(self,req):
        serializer = BookSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(data=serializer.data,message='Data added successfully.')
        else:
            return Response(serializer.errors, status=400)

class CategoryView(APIView):
    cat=Category.objects.all()
    serializer=CategorySerializer(cat,many=True)
    def get(self,req):
        return success_response(data=self.serializer.data,message='All Category Data.')
    def post(self,req):
        serializer = CategorySerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(data=serializer.data,message='Data added successfully.')
        else:
            return Response(serializer.errors, status=400)

# Anish work

class UserView(APIView):
    user = User.objects.all()
    serializer = UserSerializer(user,many=True)

    def get(self,req):
        return success_response(data = self.serializer.data,message="User Created")

    def post(self,req):
        serializer = UserSerializer(data= req.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(data = self.serializer.data,message="User Added")
        else:
            return Response(serializer.errors,status=400)




