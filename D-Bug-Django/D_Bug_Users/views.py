from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from rest_framework import status

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