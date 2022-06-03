from django.db import models


# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    contact_no = models.CharField(max_length=13)
    gender = models.CharField(max_length=10)

class Trainee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    contact_no = models.CharField(max_length=13)
    exp = models.PositiveIntegerField()
class Doubts(models.Model):
    name = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    question_from = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    answer_by = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    when_asked = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=20)


