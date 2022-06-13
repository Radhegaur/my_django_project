from django.urls import include,path
from . import views







urlpatterns = [

    path ('trainers/', views.TrainerList.as_view()),
    path('trainees/', views.TraineeList.as_view()),
    path('doubts/', views.DoubtsList.as_view()),

]


 
