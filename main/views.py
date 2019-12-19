from django.shortcuts import render

# Create your views here.


def home(request):

    context = {'active':'home'}

    return render(request,'main/index.html', context)

def products(request):

    context = {'active':'products'}

    return render(request,'main/products.html', context)