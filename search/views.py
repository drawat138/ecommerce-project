from django.shortcuts import render
from products.models import SubCategory,Products
from django.db.models import Q

# Create your views here.
def search(request):
	query=request.GET.get("search")
	subcategories=SubCategories.objects.all()
	if query is not none:
		lookups= (Q(description__icontains=query)|
			Q(brand__brandname__icontains=query)|
			Q(title__icontains=query))
		products=Products.objects.filter(lookups,status=True).distinct
		context={'products':products,
		          'subcategories':subcategories 
		        }
	else:
		products=Products.objects.all()
		context={'products':products,
		          'subcategories':subcategories 
		         }
		return render(request,'front/products.html',context)
