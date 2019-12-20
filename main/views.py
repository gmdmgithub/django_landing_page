from django.shortcuts import render

import landing_page.settings as stg

# Create your views here.

def current_path(request):

    langs = [lg for lg,_ in stg.LANGUAGES]
    c_path = request.path.split('/')
    c_path = '/'.join(c_path[2:]) if c_path[1] in langs else c_path
    print(c_path)
    return c_path

def home(request):

    context = { 'active':'home',
                'current_path':current_path(request)
                }

    return render(request,'main/index.html', context)

def projects(request):

    context = { 'active':'projects',
                'current_path':current_path(request)
                }

    return render(request,'main/projects.html', context)