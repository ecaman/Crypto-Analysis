from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader
import pandas as pd

def detail(request):
    question = "alors ?"
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    dic = {'one': [1, 2, 3], 'two': ["un", "deux", "trois"]}
    df = pd.DataFrame(dic).to_html()
    lol = "salut !"
    j = [1, 2, 3, 4, 5]
    my_max = max(j)
    affichage = "comment t'es beau"
    context = {
        'affichage': affichage,
        'lol': df,
        'j': j,
        'my_max': my_max,
        'test': 'https://www.google.com',
    }
    return HttpResponse(template.render(context, request))
