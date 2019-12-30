from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages

from django.urls import reverse
# Create your views here.

from .models import Question, Choice


def home(request):
    
    latest_question_list = Question.objects.order_by('-publish_date')
    
    context = {'title':'main page', 'latest_questions':latest_question_list}

    return render(request, 'polls/index.html', context)

def details(request, pk):
    
    details = None
    context = {'title':'details page'}

    messages.success(request, 'Please vote')

    try:
        question = Question.objects.get(pk=pk)
        context['question'] = question
    except Question.DoesNotExist:
        raise Http404("Question des not exists")

    return render(request, 'polls/details.html', context)

def results(request, pk):
    
    results = get_object_or_404(Question, pk=pk)
    context = {'title':'results page', 'question':results}

    return render(request, 'polls/results.html', context)

def vote(request, pk):

    print(request.POST.get('choice', None))

    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except: #(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))