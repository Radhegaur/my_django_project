# from dataclasses import field
from rest_framework import serializers
from .models import  Trainee, Trainer,Doubts
from xml.parsers.expat import model


class DoubtsSerializer(serializers.Serializer):
    name = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
    question_from = serializers.StringRelatedField()
    answer_by = serializers.StringRelatedField()
    when_asked = serializers.DateTimeField()
    result = serializers.CharField()




class TrainerSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Trainer
        fields = ['name','age','email','contact_no','gender']

class TraineeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trainee
        fields = ['name','age','email','contact_no','exp']

 
    

    