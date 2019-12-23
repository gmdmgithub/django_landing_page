from django.shortcuts import render
from django.http import Http404

# Create your views here.

from .models import Question, Choice


def home(request):
    
    latest_question_list = Question.objects.order_by('-publish_date')
    
    context = {'title':'main page', 'latest_questions':latest_question_list}

    return render(request, 'polls/index.html', context)

def details(request, pk):
    
    details = None
    context = {'title':'details page'}

    try:
        question = Question.objects.get(pk=pk)
        context['question'] = question
    except Question.DoesNotExist:
        raise Http404("Question des not exists")

    return render(request, 'polls/details.html', context)

def results(request, pk):
    
    results = None
    context = {'title':'details page', 'results':results}

    return render(request, 'polls/results.html', context)
