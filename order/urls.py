from importlib.resources import path

from order import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addtocard/<int:id>',views.addtocard,name='addtocart'),
    path('deletefromcart/<int:id>',views.deletefromcart,name='deletefromcart')
]