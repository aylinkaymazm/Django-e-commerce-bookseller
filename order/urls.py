from django.urls import path

from order import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addtocart/<int:id>/<slug:slug>',views.addtocart,name='addtocart'),
    path('deletefromcart/<int:id>',views.deletefromcart,name='deletefromcart'),
    path('orderproduct/',views.orderproduct,name='orderproduct'),


]
