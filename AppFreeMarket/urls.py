from django.urls import path
from AppFreeMarket import views

urlpatterns = {
    path('', views.home, name='Home'), 
    path('buyer', views.buyer, name='Buyer'),
    path('seller', views.seller, name='Seller'),
    path('delivery', views.delivery, name='Delivery'),
    path('searchDelivery', views.searchDelivery, name='SearchDelivery'),
    path('search/', views.search),
}