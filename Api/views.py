from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from . serializers import UserSerializer
from . models import User

from rest_framework.decorators import APIView, api_view,permission_classes,authentication_classes




@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def eventList(request):
    events = User.objects.all()
    serializer = UserSerializer(events,many=True,context={'request':request})
    return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def eventDetail(request,pk):
    events = User.objects.get(id=pk)
    serializer = UserSerializer(events,many=False,context={'request':request})
    return Response(serializer.data)






@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def eventCreate(request):
    serializer = UserSerializer(data = request.data,context={'request':request})
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def eventUpdate(request,pk):
    event = User.objects.get(id=pk)
    serializer = UserSerializer(instance=event,data=request.data,context={'request':request})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def eventDelete(request,pk):
    event = User.objects.get(id=pk)

    event.delete()
    
    
    return Response('data is deleted')

