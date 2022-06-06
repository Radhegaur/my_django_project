from dataclasses import field
from rest_framework import serializers
from .models import Trainee, Trainer,Doubts
class TrainerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Trainer
        fields = "__all__"

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = "__all__"
class DoubtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doubts
        fields = "__all__"
