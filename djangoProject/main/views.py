from django.shortcuts import render
from . import logic
from django.template import Context

# Create your views here.


def index(response):
    temp = logic.get_amazon_results()
    context = {'data': temp}
    return render(response, 'main/index.html', context=context)
