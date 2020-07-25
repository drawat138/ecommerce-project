from django.shortcuts import render,redirect
from .models import Cart
from products.models import Products

# Create your views here.
def cart(request):
	cart_obj,cart_created=Cart.objects.new_or_get(request)
	context={'cart':cart_obj}
	return render(request,'cart/cart.html',context)
def cartupdate(request):
	product_id=request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj=Products.objects.get(id=product_id)
		except Products.DoesNotExist:
			return redirect('/cart')
		cart_obj,cart_created=Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session['cart_items']=cart_obj.products.count()
		return redirect('/cart')

def checkout(request):
	return render(request,'cart/checkout.html',context)