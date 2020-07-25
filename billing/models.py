from django.db import models
from accounts.models import UserProfile
from django.db.models.signals import post_save

# Create your models here.
class BillingProfileManager(models.Manager):
	def new_or_get(self,request):
		user=None
		if 'username' in request.session:
			user=UserProfile.objects.get(email=request.session['username'])
			guest_email_id=request.session.get('guest_email_id')
			created=False
			obj=None
		if user is not None:
			obj.created=self.models.objects.get_or_create(user=user,email=user.email)
		elif guest_email_id is not None:
			guest_email_obj=GuestEmail.objects.get(id=guest_email_id)
			obj.created=self.model.objects.get_or_create(email=guest_email_obj.email)
		else:
			pass
		return obj.created
	def user_created_reciever(sender,instance,created,*args,**kwargs):
		if created and instance.email:
			BillingProfile.objects.get_or_create(user=insatance,email=insatance.email)
	post_save.connect(user_created_reciever,sender=UserProfile)

class BillingProfile(models.Model):
	user=models.OneToOneField(UserProfile,null=True,blank=True,on_delete=models.CASCADE)
	email=models.EmailField()
	active=models.BooleanField(default=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)
def __str__(self):
	return self.email

