from rest_framework import serializers
from .models import Trainer
class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Trainer
        fields = "__all__"