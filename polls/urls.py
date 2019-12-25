from django.urls import path
from . import views

# namespace
app_name = 'polls'

urlpatterns = [
    
    path( '', views.home,  name='main'),

    path( 'details/<str:pk>', views.details,  name='details'),
    path( 'results/<str:pk>', views.results,  name='results'),
    path( 'vote/<str:pk>', views.vote,  name='vote'),

]