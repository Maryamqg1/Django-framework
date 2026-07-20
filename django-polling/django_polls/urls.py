from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.VoteView.as_view(), name="vote"),
    path("<int:pk>/choice/", views.ChoiceView.as_view(), name="choice"),
    path("home/", views.Homeview.as_view(), name="home"),
    path("terms/", views.TermsView.as_view(), name="terms"),
    path("create/", views.PollCreateView.as_view(), name="create"),
    path("register/", views.UserRegisterView, name="register"),
    
    # path("update/<int:pk>/",views.PollUpdateView.as_view(),name="update",),
]


# app_name = "polls"
# urlpatterns = [
#     # path('', views.index, name='index'),
#     path('', views.IndexView.as_view(), name='index'),
#     path('mission/', views.mission, name='Mission'),
#     path('intro/', views.intro, name='Intro' ),
#     path('choice/', views.choice, name='choice'),
#     # path('<int:question_id>/', views.details, name='details'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
        
#     ]

# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
