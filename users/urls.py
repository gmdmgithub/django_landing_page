from django.urls import path, reverse_lazy
# from django.conf.urls import include, url
from . import views


from django.contrib.auth import views as auth_views

app_name='profiles'

urlpatterns = [
    # url(r'^', include('django.contrib.auth.urls')),
    path('register',views.register, name='register'),
    path('profile',views.profile, name='profile'),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

        
    

    # path('login',views.login, name='login'),
    # path('login',views.logout, name='login'),
]