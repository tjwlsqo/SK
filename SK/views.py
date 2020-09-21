from django.db import connection
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class Gettest(APIView):
    def get(self,requset,format=None):
        st="{" \
           "\"version\": \"2.0\"," \
           "\"resultCode\": \"OK\"," \
           "\"output\": {" \
           "\"datetime\": \"오늘\"," \
           "\"TEST\": \"테에스트\"," \
           "}," \
           "}"
        return Response(st)



