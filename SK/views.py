from django.db import connection
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class Gettest(APIView):
    def get(self,requset,format=None):
        return Response("test")

