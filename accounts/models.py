from django.db import models

# Create your models here.
GENDER_CHOICE=(('male','male'),('female','female'),('other','other'))
class UserProfile(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(unique=True)
	phone=models.CharField(max_length=10,unique=True)
	gender=models.CharField(max_length=7,choices=GENDER_CHOICE)
	password=models.CharField(max_length=10)
	confirm_password=models.CharField(max_length=10)