from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from product.models import Category


def index(request):

    category = Category.objects.all()
    context ={'categor':category}
    return render(request,'user_profile.html',context)
