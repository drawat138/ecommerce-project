from django import forms
from .models import UserProfile
class RegistrationForm(forms.ModelForm): 
	def clean_password(self):
		data=self.cleaned_data
		password=self.cleaned_data.get('password')
		confirm_password=self.cleaned_data.get('confirm_password')
		if password==confirm_password:
			return data
		else:
			raise forms.ValidationError("password and confirm password does not match")


	def clean_email(self):
		data=self.cleaned_data
		email=self.cleaned_data.get('email')
		qs=UserProfile.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		else:
			return email
	def clean_phone(self):
		data=self.cleaned_data
		phone=self.cleaned_data.get('phone')
		qs=UserProfile.objects.filter(phone=phone)
		if qs.exists():
			raise forms.ValidationError("Number already exists")
		else:
			return phone

	class Meta:
		model=UserProfile
		fields='__all__'
		widgets={
			'name':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':'enter name',
		           }),
			'email':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'enter email'
				}),
			'phone':forms.TextInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter moblie no',
		        }),
			'password':forms.PasswordInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter password',
		        }),
			'confirm_password':forms.PasswordInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter confirm password',
		        }),
			'gender':forms.Select(attrs={
		        'class':'form-control',
		 
		})
			
		}
class LoginForm(forms.Form):
	username= forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'enter email address',
		}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'enter password',
		}))