from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

app_name='posts'

urlpatterns = [
    # path('',views.home, name='main'),
    path('', PostListView.as_view(), name='main'), #class based approach
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'), #class based approach
    path('new', PostCreateView.as_view(), name='post-create'), #class based approach
]