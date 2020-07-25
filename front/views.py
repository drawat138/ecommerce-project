from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from accounts.forms import LoginForm
from accounts.models import UserProfile
from django.http import HttpResponse
from products.models import Products,Review,SubCategory
from products.forms import ReviewForm
from cart.models import Cart
# Create your views here.
def register(request): 
	form=RegistrationForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return redirect('/login')
	context={'form':form}
	return render(request,'front/register.html',context)

def login(request):
	form=LoginForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			try:
				user=UserProfile.objects.get(email=username,password=password)
				request.session['username']=user.email
				return redirect("/products")
			except:
				return HttpResponse("<p>Login failed</p>")

	context={'form':form}
	return render(request,'front/login.html',context)
	
def home(request):
	return render(request,'front/home.html')
def products(request):
	products=Products.objects.all()
	subcategories=SubCategory.objects.all()
	context={'products':products,
	          'subcategories':subcategories
	        }
	return render(request,'front/products.html',context)

def productbycategory(request,id):
	subcategories=SubCategory.objects.all()
	products=Products.objects.filter(subcategoryname=id)
	context={'products':products,
	'subcategories':subcategories
	}
	return render(request,'front/products.html',context)

def productdetails(request,id):
	if 'username' not in request.session:
		reviewform = ReviewForm(request.POST or None)
	else:
		reviewform= ReviewForm(request.POST or None, initial={'review_by':request.session['username'],'product_id':id})

	if request.method== "POST":
		if reviewform.is_valid():
			review_by=reviewform.cleaned_data.get('review_by')
			description=reviewform.cleaned_data.get('description')
			review=Review(review_by=review_by,description=description,product_id=id)
			try:
				review.save()
			except:
				return HttpResponse("<h1> Unable to sumbit review. </h1>")
	product=Products.objects.get(id=id)
	reviews=Review.objects.filter(product_id=id)
	cart_obj,cart_created=Cart.objects.new_or_get(request)
	context={'product':product,
	'reviewform':reviewform,
	'reviews':reviews, 
	'cart':cart_obj
	}
	return render(request,'front/productdetails.html',context)  

def logout(request):
	for key in list(request.session.keys()):
		del request.session[key]
	return redirect('/login')

	
