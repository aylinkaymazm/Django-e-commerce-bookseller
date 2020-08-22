from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import product
from home.forms import SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu, UserProfile, FAQ
# context e yolla burdan render la index.html e yolluyoruz.
from order.models import ShopCart
from product.models import Product, Category, Images


def index(request):
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:3]
    category = Category.objects.all()
    dayproducts=Product.objects.all()[:4]
    lastproducts= Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    context = {'setting': setting,
               'category': category,
               'page':'home',
               'sliderdata': sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts':randomproducts,
               'product':product,
               }
    return render(request,'index.html',context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    context = {'setting': setting,
               'category':category,
               'page':'home'}
    return render(request,'hakkimizda.html',context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'page': 'home'}
    return render(request,'referanslarimiz.html',context)


def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data= ContactFormMessage()
            data.name= form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip =request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"mesajınız başarı ile gönderilmiştir.Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,
               'form':form,
               'category':category,
               }
    return render(request,'iletisim.html',context)


def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Product.objects.filter(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products':products,
               'category':category,
               'categorydata ':categorydata,
               }
    return render(request,'products.html',context)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'product': product,
               'category': category,
               'images':images,
               }
    return render(request,'product_detail.html',context)

def content_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.filter(category_id=id)
    link='/product/'+str(product[0].id)+'/'+product[0].slug
    #return HttpResponse(link)
    return HttpResponseRedirect(link)

def logout_view(request):
    logout(request)
    return  HttpResponseRedirect('/')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user=request.user
            userprofile=UserProfile.objects.filter(user_id=current_user.id)
            request.session['userimage']=userprofile[0].image.url
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatalı !Kullanıcı adınızı yada şifreyi yanlış girdiniz.")
            return HttpResponseRedirect('/login')


    category = Category.objects.all()
    context = {'category':category,
              }
    return render(request,'login.html',context)

def signup_view(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            current_user = request.user
            data = UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request,"Hoşgeldiniz...")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category':category,
               'form': form,
              }
    return render(request,'signup.html',context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {'category': category,
               'faq': faq,
               }

    return render(request, 'faq.html', context)