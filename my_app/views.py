# from urllib import response
# from django.shortcuts import render
# from my_app.models import Trainer,Trainee,Doubts
# from my_app.models import Doubts
# from .serializers import TrainerSerializer
# from .models import Trainee, Trainer,Doubts
# from rest_framework.decorators import api_view
# from django.http import HttpResponse 


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from my_app import serializers

from my_app.models import Trainer,Trainee,Doubts
from my_app.serializers import TraineeSerializer, TrainerSerializer,DoubtsSerializer





@api_view(['GET', 'PUT', 'DELETE'])
def trainer_api(request, id):
    trainer = get_object_or_404(Trainer, pk=id)

    # try:
    #     Trainer.objects.get(pk=id)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrainerSerializer(trainer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def trainer_post(request):
    serializer = TrainerSerializer(Trainer, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)







@api_view(['GET', 'PUT', 'DELETE'])
def trainee_api(request, id):
    trainee = get_object_or_404(Trainee, pk=id)

    # try:
    #     Trainee.objects.get(pk=id)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TraineeSerializer(trainee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TraineeSerializer(trainee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        trainee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
@api_view(['GET', 'PUT', 'DELETE'])
def doubts_api(request, id):
    doubts = get_object_or_404(Doubts, pk=id)

    # try:
    #     Trainee.objects.get(pk=id)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoubtsSerializer(doubts)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoubtsSerializer(doubts, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        doubts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    