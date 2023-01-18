from django.db import models

# Create your models here

class Question(models.Model):
    question = models.CharField(max_length=3000)
    answer = models.CharField(max_length=3000)

    def __str__(self):
        return self.question

class Score(models.Model):
    score = models.CharField(max_length=10)

    def __str__(self):
        return self.score