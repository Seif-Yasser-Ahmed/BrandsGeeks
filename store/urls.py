from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logoutUser, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),
    path('checkout/typage/', views.typage, name="typage"),
    path('typage2/', views.typage2, name="typage2"),
    path('contactus/', views.contactus, name="contactus"),
    path("add_to_cart", views.add_to_cart, name="add"),
]
