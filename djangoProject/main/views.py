from django.shortcuts import render
from . import logic
from django.template import Context

# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'main/index.html')
    return render(request, 'main/index.html')


def result(request):
    context = {'data': request.POST['url']}
    return render(request, 'main/results.html', context)
