from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

app_name='posts'

urlpatterns = [
    # path('',views.home, name='main'),
    path('', PostListView.as_view(), name='main'), #class based approach
    path('user/<str:username>', UserPostListView.as_view(), name='user-main'), #class based approach
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'), #class based approach
    path('new', PostCreateView.as_view(), name='post-create'), #class based approach
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'), #class based approach
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), #class based approach
]