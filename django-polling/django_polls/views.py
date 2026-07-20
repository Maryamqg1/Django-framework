from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import View, generic
from django.utils import timezone
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Choice, Poll, Question
from django.contrib.auth.models import User
from django.shortcuts import redirect


def UserRegisterView(request):
    """
    Handle user registration with register.html template.
    Supports both GET (display form) and POST (process registration) requests.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(
                request, 
                "Registration successful! Please check your email to activate your account."
            )
            return redirect('polls:index')
        else:
            # Form has errors, they will be displayed in the template
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
        'page_title': 'User Registration',
    }
    return render(request, 'polls/register.html', context)



class PollCreateView(generic.CreateView):
    model = Poll
    fields = ["question"]
    template_name = "polls/poll.html"
    success_url = "/polls/home/"

# class PollUpdateView(generic.UpdateView):
#     model = Poll
#     fields = ["question"]
#     template_name = "polls/update_poll.html"
#     success_url = "/polls/home/"

class Homeview(generic.TemplateView):
    template_name = "polls/home.html"

class TermsView(generic.TemplateView):
    template_name = "polls/T&c.html"

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by("-pub_date")[:5]
    
    def get_queryset(self):
        
        """
    Return the last five published questions (not including those set to be
    published in the future).
    """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"
    
class ChoiceView(generic.DetailView):
    model = Question
    template_name = "polls/choice.html"
    context_object_name = "question"

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_of_choices"] = self.object.choice.all()
        return context
    
    

class VoteView(View):
    '''check for reasons why it dosent allow for  get request'''
    
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        
        try:
             selected_choice = question.choice.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(
                request,
                "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
  

# Create your views here.

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/details.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# basic class based view

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:3]
    #template = loader.get_template('polls/index.html')
    #context = {"latest_question_list": latest_question_list}
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html',{'latest_question_list': latest_question_list})
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse('Hello, world. You are at the polls index.')

# def choice(request):
    #All = Question.objects.all()
    #choices = Choice.objects.all()
    #odds = [x for x in choices if x.id %2 != 0]
    #filtered_odds = filter(lambda x: x.id %2 != 0, choices) #didn't execute properly
    #return render(request, 'polls/choice.html', ({'odds': odds})) #, 'filtered_odds': filtered_odds
    # for odd_id in All:
    #     if odd_id.id %2 !=0:
    #         return odd_id
    #     else:
    #         print ('Unacceptable id no.')
    #odd_id = Question.objects.filter(id__exact = 1)
    # latest_question_list = Question.objects.last()
    # list_of_choices =latest_question_list.choice.all()
    # template = loader.get_template('polls/choice.html')
    
    # return HttpResponse(template.render({'list_of_choices': list_of_choices,
    #                                      'latest_question_list': latest_question_list},request))
    
# def details (request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id) 
    # except Question.DoesNotExist:
    #     raise Http404 ('This Question does not exist')
    # return render(request, 'polls/details.html',{'question':question})   

def mission(request):
    return HttpResponse('Mission accomplished.')


# def my_view(request):
#     context = {'foo': 'bar'}
#     return HttpResponse(request, 'myapp/index.html', context)

def intro(request):
    return HttpResponse('Greetings, Welcome to to our website')

# def detail(request, question_id):
#     return HttpResponse("How can we be of Assitance to you %s ?" % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/result.html", {"question": question})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
    



