from django.shortcuts import render, HttpResponse, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #user can do after login second - can update only this one he created

from django.http import Http404, HttpResponseRedirect, JsonResponse

from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.models import User

#different approach - class based view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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

    paginate_by = 5 # using pagination in class view - originally comes from django.core.paginator import Paginator

class UserPostListView(ListView):
    model = Post
    template_name='posts/user_posts.html'  # <app>/<model>_<viewtype>.html - standard naming convention 
    context_object_name = 'posts'
    # ordering =['-post_date']  - its overwrite by get_queryset

    paginate_by = 5 # using pagination in class view - originally comes from django.core.paginator import Paginator

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-post_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # with UserPassesTestMixin we can use this func to check if its ok
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:main')

    # two ways to check and be redirect

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if self.object.author == request.user:
    #         self.object.delete()
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         raise Http404 #or return HttpResponse('404_url')
    
    def test_func(self): # with UserPassesTestMixin we can use this func to check if its ok
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False