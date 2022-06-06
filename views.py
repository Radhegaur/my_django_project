
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from doubts.models import Trainer
from doubts.serializers import TrainerSeializer


@api_view(['GET', 'PUT', 'DELETE'])
def trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)

    # try:
    #     Trainer.objects.get(pk=id)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrainerSeializer(trainer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrainerSeializer(trainer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def trainer_post(request):
    serializer = TrainerSeializer(trainer, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
