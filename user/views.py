from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from home.models import UserProfile
from order.models import Order, OrderProduct
from product.models import Category
from user.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user

    profile =UserProfile.objects.get(user_id=current_user.id)
    context ={'category':category,
              'profile':profile}
    return render(request,'user_profile.html',context)

@login_required(login_url='/login')
def user_update(request):
    if request.method =='POST':
        user_form =UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'hesabınız Güncelledi !!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        context={
            'category':category,
            'user_form':user_form,
            'profile_form':profile_form,
        }
        return render(request,'user_update.html',context)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.<br>'+str(form.errors) )
            return HttpResponseRedirect('/user/password')

    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
        'form': form,'category': category,
    })
@login_required(login_url='/login')  # Check Login
def orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'orders': orders,
    }
    #return HttpResponse("product Listesi")
    return render(request,'user_orders.html',context)

@login_required(login_url='/login')  # Check Login
def orderdetail(request,id):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id,id=id)   #güvenlik açığını önlemek için..
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {'category': category,
               'order': order,
               'orderitems': orderitems,
               }
    #return HttpResponse(str(id))
    return render(request, "user_orders.html", context)