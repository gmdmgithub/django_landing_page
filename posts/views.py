from django.shortcuts import render, HttpResponse

from django.http import Http404, HttpResponseRedirect, JsonResponse

from .models import Post

#different approach - class based view
from django.views.generic import ListView, DetailView

#dummy data to avoid DB 
posts = [
    {
        'author': 'Alex Magic',
        'title': 'Basketbal',
        'content': 'The basketball is the best game',
        'post_date':'2020-01-01',
        'id': 1,
    },
    {
        'author': 'Cristiano Ronaldo',
        'title': 'Football',
        'content': 'The footbal is the best game',
        'post_date':'2020-01-02',
        'id': 2,
    }
]

def home(request):
    # return HttpResponse('Hi there')

    post_db = Post.objects.all()

    context = {
            'title':'main post page', 
            'posts':post_db
        }

    return render(request,'posts/main.html', context)


class PostListView(ListView):
    model = Post
    template_name='posts/main.html'  # <app>/<model>_<viewtype>.html - standard naming convention 
    context_object_name = 'posts'
    ordering =['-post_date']

class PostDetailView(DetailView):
    model = Post