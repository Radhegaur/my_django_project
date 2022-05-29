from django.shortcuts import render
from django.http import HttpResponse

from my_app.models import Trainer

# def about_my_app(request):
#     return HttpResponse ("This is my first django app ! ")
# def index (request):
#     return HttpResponse ("This is another comment ")





def about_my_app(request):
    trainer_list = Trainer.objects.all()
    for trainer in trainer_list:
        print(trainer.name)
        



    return HttpResponse ("This is my first django app ! ")