from django.urls import path
from . import views

urlpatterns=[
        path('cart/',views.cart),
        path('cartupdate/',views.cartupdate),
        path('checkout/',views.checkout),
]