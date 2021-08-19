from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from . serializers import UserSerializer
from . models import User

from rest_framework.decorators import APIView, api_view



@api_view(['GET'])
def eventList(request):
    events = User.objects.all()
    serializer = UserSerializer(events,many=True,context={'request':request})
    return Response(serializer.data)



@api_view(['GET'])
def eventDetail(request,pk):
    events = User.objects.get(id=pk)
    serializer = UserSerializer(events,many=False,context={'request':request})
    return Response(serializer.data)






@api_view(['POST'])
def eventCreate(request):
    serializer = UserSerializer(data = request.data,context={'request':request})
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def eventUpdate(request,pk):
    event = User.objects.get(id=pk)
    serializer = UserSerializer(instance=event,data=request.data,context={'request':request})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def eventDelete(request,pk):
    event = User.objects.get(id=pk)

    event.delete()
    
    
    return Response('data is deleted')

