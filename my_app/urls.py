from django.urls import path

from . import views

urlpatterns = [
    path ('',views.about_my_app,name='about_my_app'),
    # path ('',views.index, name= 'index'),
]