from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

	class Meta:
		model=Review
		fields=['review_by','product_id','description']
		widgets={
		'review_by':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':'enter email',
		           'readonly':'readonly'
		           }),
		'product_id':forms.TextInput(attrs={

				'class':'form-control',
				'readonly':'readonly',
				'type':'hidden'
				}),
		'description':forms.Textarea(attrs={
		        'class':'form-control',
		        'placeholder':'enter description',
		        }),
		}