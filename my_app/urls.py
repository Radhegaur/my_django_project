from django.urls import include,path
from . import views



urlpatterns = [
    
    path('trainers/', views.trainer_post),
    path ('trainers/<int:id>/', views.trainer_api),
    path('trainee/<int:id>/', views.trainee_api),
    path('doubts/<int:id>/', views.doubts_api),

    
]


 
