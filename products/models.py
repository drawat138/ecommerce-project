from django.db import models
import random
import os

def get_filename_extension(filename):
	basename=os.path.basename(filename)
	name,ext=os.path.splitext(basename)
	return name,ext

def upload_productimage(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "products/"+f"{new_filename}/{final_filename}"


# Create your models here.
class Category(models.Model):
	categoryname=models.CharField(max_length=30,unique=True)
	categoryimage=models.ImageField(blank=True,null=True,unique=True)
	def __str__(self):
		return self.categoryname

class SubCategory(models.Model):
	categoryname=models.ForeignKey(Category,on_delete=models.CASCADE)
	subcategoryname=models.CharField(max_length=30)
	subcategoryimage=models.ImageField(blank=True,null=True)
	def __str__(self):
		return self.categoryname.categoryname+" - "+self.subcategoryname
class Brand(models.Model):
	brandname=models.CharField(max_length=80,unique=True)
	brandimage=models.ImageField(blank=True,null=True)
	def __str__(self):
		return self.brandname
class Products(models.Model):
	brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
	subcategoryname=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	title=models.CharField(max_length=80)
	description=models.TextField()
	
	price=models.DecimalField(decimal_places=2,max_digits=10)
	productimage=models.ImageField(upload_to= upload_productimage)
	discount=models.IntegerField()
	status=models.BooleanField(default=True)
	createdat=models.DateTimeField(auto_now_add=True)
	updatedat=models.DateTimeField(auto_now=True)
	slug=models.SlugField(blank=True,null=True)

class Review(models.Model):
	review_by=models.EmailField()
	product_id=models.IntegerField()
	description=models.TextField()
	createdat=models.DateTimeField(auto_now_add=True)
	updatedat=models.DateTimeField(auto_now=True)