from .models import Trainee, Trainer,Doubts

from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from my_app import serializers
from my_app.models import Trainer,Trainee,Doubts
from my_app.serializers import TraineeSerializer, TrainerSerializer,DoubtsSerializer
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend


# generic view

class TrainerList(ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['age']
class TraineeList(ListAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]
class DoubtsList(ListAPIView):
    queryset = Doubts.objects.all()
    serializer_class = DoubtsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']








# class TrainerListCreate(generics.ListCreateAPIView):
#     serializer_class = TrainerSerializer

#     def get_queryset(self):
     
#         queryset = Trainer.objects.all()
#         user = self.request.user
#         return Trainer.objects.filter(user_name= user)

