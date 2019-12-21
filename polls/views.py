from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'test':'Nice to see you!'}
    return render(request, 'polls/index.html', context)
