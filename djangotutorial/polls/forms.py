from django.forms.models import ModelForm
from . models import Question, Choice, Grade

class Modelform ('forms.ModelForm'):
    model = Question
    fields = ['question_text', 'pub_date']
    
 
