from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.trainer_post),
    path('trainers/<int:id>/',  views.trainer_api),
]
