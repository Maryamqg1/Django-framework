from django.http import HttpResponse
from .models import Question, Choice , Grade
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:3]
    template = loader.get_template('polls/index.html')
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse('Hello, world. You are at the polls index.')

def detail(request):
    last_question = Question.objects.last()
    list_of_choices =last_question.choice.all()
    template = loader.get_template('polls/choice.html')
    return HttpResponse(template.render({'list_of_choices':list_of_choices},request))
    

def mission(request):
    return HttpResponse('Mission accomplished.')


# def my_view(request):
#     context = {'foo': 'bar'}
#     return HttpResponse(request, 'myapp/index.html', context)

def intro(request):
    return HttpResponse('Greetings, Welcome to to our website')

def detail(request, question_id):
    return HttpResponse("How can we be of Assitance to you %s ?" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    



