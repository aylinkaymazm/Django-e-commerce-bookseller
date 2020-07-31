from typing import Dict

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text="hey django "
    context = {'text': text}
    #context e yolla burdan rendell la index.html e yolluyoruz.
    return render(request, 'index.html', context)