from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from home.models import UserProfile
from product.models import Category

@csrf_exempt
def index(request):
    category = Category.objects.all()
    current_user = request.user

    profile =UserProfile.objects.get(pk=current_user.id)
    context ={'category':category,
              'profile':profile}
    return render(request,'user_profile.html',context)


class UserUpdateForm(object):
    pass


class ProfileUpdateForm(object):
    pass


@login_required(login_url='/login')
def user_update(request):
    if request.method =='POST':
        user_form =UserUpdateForm(request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Hoşgeldiniz!!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request)
        context={
            'category':category,
            'user_form':user_form,
            'profile_form':profile_form
        }
        return render(request,'user_update.html')





