from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse,HttpResponse
from rest_framework import status
import requests


# Create your views here.
@api_view(['GET','POST'])
def ProfileFunc(request,format=None):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        profile = ProfileSerializer(data = data)
        if profile.is_valid():
            profile.save()
            return JsonResponse(profile.data, status = status.HTTP_201_CREATED)
        return JsonResponse(profile.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        profiles = Profile.objects.all()
        profiles = ProfileSerializer(profiles,many=True)
        return Response(profiles.data)

@api_view(['GET','PUT','DELETE'])
def ProfileDetails(request,name,format=None):
    try:
        profile = Profile.objects.get(name=name)
    except Profile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        profile = ProfileSerializer(profile,data=data)
        if profile.is_valid():
            profile.save()
            return JsonResponse(profile.data)
        return JsonResponse(profile.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

owner = 'thesmartcoder7'
access_token = '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'
headers = {'Authorization':'Token' + access_token}

url = f'https://api.github.com/users/{owner}/repos'
repos = requests.get(url,headers=headers).json()
lans = [ls['language'] for ls in repos]
languages = dict()
for lan in lans:
    if lan in languages:
        languages[lan] += 1
    else:
        languages[lan] = 1
    
print(languages)