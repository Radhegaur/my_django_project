from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http import HttpResponse
from my_app.models import Trainer
from .serializers import TrainerSerializer
from .models import Trainer
from .models import Doubts
from rest_framework.decorators import api_view
from rest_framework import viewsets


@api_view(['GET','PUT','POST','DELETE'])
def trainer_api(request):
    if request.method == 'GET':
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(Trainer,many=True)
        return response(serializer.data)

    elif request.method == 'POST':
        trainer_data = JSONParser().parse(request)
        trainer_serializer = TrainerSerializer(data=trainer_data)
        if trainer_serializer.is_valid():
            trainer_serializer.save()
            return JsonResponse(trainer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(trainer_serializer.errors, status=status.HTTP_400_BAD_RE)



    elif request.method == 'PUT':
        trainer_data = JSONParser().parse(request) 
        trainer_serializer = TrainerSerializer(trainer, data=trainer_data) 
        if trainer_serializer.is_valid(): 
            trainer_serializer.save() 
            return JsonResponse(trainer_serializer.data) 
        return JsonResponse(trainer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    elif request.method =='DELETE':
        trainer.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
















# class TrainerViewSet(viewsets.ModelViewSet):
#     queryset = Trainer.objects.all().order_by('name')
#     serializer_class = TrainerSerializer




# def about_my_app(request):
    # counts = Doubts.objects.filter(question_from__id=24).count()

    # print(counts)

    # doubts= Doubts.objects.filter(
    #     answer_by__id__icontains="base").select_related("answer_by")
    # for doubt in doubts:
    #     print("question",doubts.question)
    #     print("answer",doubts.answer_by.name)
    # trainer=Trainer.objects.filter(name="ram")
    # print(trainer)
    # return HttpResponse ("This is my first django app ! ")
# def index (request):
#     return HttpResponse ("This is another comment ")


# def about_my_app(request):
    
    # trainer_list = Trainer.objects.all()
#     # print(trainer_list)

    # for trainer in trainer_list:

        # print(trainer.name)
        # print(trainer.email)
        # print(trainer.contact_no)
        #print(Trainer.objects.defer("name", "age"))

        # print(trainer.defer("name","age"))

        # return HttpResponse ("This is my first django app ! ")

# insert = Trainer(name="ram",age='25',email='ram@gmail.com',contact_no='5689547856',gender='Male')
# insert.save()

