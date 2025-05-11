from django.urls import path
from vegitables import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index',views.index),
    path('shop',views.shop),
    path('register',views.register),
    path('login',views.user_login),
    path('addtocart/<pid>',views.addtocart),
    path('product',views.product),
    path('',views.product),
    path('vegetables',views.vegetables),
    path('cart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('remove/<cid>',views.removecart),
    path('logout',views.user_logout),
    path('contact',views.contact),
    path('fruits',views.fruits),
    path('non-veg',views.nonveg),
    path('checkout',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.success),
    # path('offer',views.offer),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)