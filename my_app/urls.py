from django.urls import include,path
from . import views

from rest_framework.routers import DefaultRouter
from my_app.views import TrainerViewSet,TraineeViewSet,DoubtsViewSet


# for viewsets patter

router = DefaultRouter()
router.register('trainers', TrainerViewSet)
router.register('trainees', TraineeViewSet)
router.register('doubts', DoubtsViewSet)
urlpatterns = router.urls


# urlpatterns = [
    
    # path('trainers/', views.trainer_post),
    # path('doubts/', views.doubts_post),
    # path ('trainers/<int:id>/', views.trainer_api),
    # path('trainee/<int:id>/', views.trainee_api),
    # path('doubts/<int:id>/', views.doubts_api),

    # path('classviewtrainer/',views.Trainers.as_view()),
    # path('classviewtrainee/',views.Trainees.as_view()),
    # path('classviewdoubt/',views.Doubt.as_view()),

    # path('trainers/',views.TrainerListCreate.as_view()),
    # path('trainees/',views.TraineeListCreate.as_view()),
    # path('doubts/',views.DoubtsListCreate.as_view()),
    
# ]


 
