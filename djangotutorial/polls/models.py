import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def was_published_recently(self):
        return self.pub_date >= timezone() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class Grade(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='type')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='grade')
    
    def __str__(self):
        return f"{self.question} - {self.choice}"
    