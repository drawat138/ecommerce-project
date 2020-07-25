from django.db import models
from products.models import Products
from django.db.models.signals import m2m_changed,pre_save
from accounts.models import UserProfile
from decimal import Decimal
# Create your models here.
class CartManager(models.Manager):
	def new_or_get(self,request):
		cart_id=request.session.get("cart_id",None)
		qs=self.get_queryset().filter(id=cart_id)
		if qs.count()==1:
			cart_obj=qs.first()
			cart_created=False
			if request.session.get('username') is not None and cart_obj.user is None:
				try:
					cart_obj=user=UserProfile.object.get(email=request.session.get('username')).id
				except:
					cart_obj.user=None
				cart_obj.save()
		else:
			try:
				user=UserProfile.objects.get(email=request.session.get('username'))
			except:
				user=None
				cart_obj=Cart.objects.new(request,user=user)
				cart_created=True
				request.session['cart_id']=cart_obj.id
		return cart_obj,cart_created
	def new(self,request,user=None):
		user_obj=None
		if user is not None:
			if request.session.get('username'):
				user_obj=user
		return self.model.objects.create(user=user_obj)

class Cart(models.Model):
	user=models.ForeignKey(UserProfile,null=True,blank=True,on_delete=models.CASCADE)
	products=models.ManyToManyField(Products,blank=True)
	subtotal=models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
	total=models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
	createdat=models.DateTimeField(auto_now_add=True)
	updatedat=models.DateTimeField(auto_now=True)

	objects=CartManager()

def m2m_updated_cart(sender,instance,action,*args,**kwargs):
 	if action=="post_add" or action=="post_remove" or action=="post_clear":
 		products=instance.products.all()
 		sum=0
 		for product in products:
   			sum=sum+product.price
   			if instance.subtotal!=sum:
   				instance.subtotal=sum
   				instance.save()
   				m2m_changed.connect(m2m_updated_cart,sender=Cart.products.through)

def pre_save_cart_total_reciever(sender,instance,*args,**kwargs):
	if instance.subtotal>0:
		instance.total=Decimal(instance.subtotal) * Decimal(1.10)
	else:
		instance.total=0.00
		pre_save.connect(pre_save_cart_total_reciever,sender=Cart)
