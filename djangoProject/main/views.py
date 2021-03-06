from django.shortcuts import render
from .scrappers import driver as dr

# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'main/index.html')
    return render(request, 'main/index.html')


def result(request):
    det = dr.driver(request.POST['url'])
    context = {'dataA': det[0], 'priceA': det[1], 'linkA': det[2]}
    return render(request, 'main/results.html', context)
