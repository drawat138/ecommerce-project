from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('',views.home),
    path('products/',views.products),
    path('productdetails/<id>',views.productdetails),
    path('logout/',views.logout),
    path('productbycategory/<id>',views.productbycategory),
]