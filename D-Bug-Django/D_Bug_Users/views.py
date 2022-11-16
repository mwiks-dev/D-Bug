from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from .models import *

# Create your views here.
class GenerateUserCredential(APIView):
    def get(self,request,format=None):
        results = self.request.query_params.get('type')
        response = {}
        r = requests.get('')
        r_status = r.status_code
        if r_status == 200:
            data = json.loads(r.json)
            for credentials in data:
                user = User(user_id='',name=credentials)
                user.save()
        else:
            response['status'] = r.status_code
            response['message'] = 'Success'
            response['credentials'] = {}
            
        return Response(response)
