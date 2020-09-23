from django.db import connection
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

import json


class Gettest(APIView):
    def get(self, requset, format=None):
        print('abc')
        dic = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {
                "datetime": "오늘""",
                "test": "테에스트",
                "response": "더럽게 안되네 씨발거"
            }
        }
        jsdic = json.dumps(dic)

        print(jsdic)
        return Response(jsdic)
