from django.urls import path
from .views import PostListView, PostDetailView
from . import views

app_name='posts'

urlpatterns = [
    # path('',views.home, name='main'),
    path('', PostListView.as_view(), name='main'), #class based approach
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), #class based approach
]