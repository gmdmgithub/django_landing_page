from django.urls import path
from . import views

# namespace
app_name = 'polls'

urlpatterns = [
    
    path( '', views.home,  name='main'),

    path( 'details/<str:pk>', views.details,  name='p_details'),
    path( 'results/<str:pk>', views.results,  name='p_results'),

]