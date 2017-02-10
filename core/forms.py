from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class GuestForm(forms.Form):
	guestName = forms.CharField(max_length=100, required=False)
	guestEmail = forms.EmailField(max_length=100, required=False)

class ItemForm(forms.Form):
	itemName = forms.CharField(max_length=100, required=False)
	itemQtt = forms.CharField(max_length=100, required=False)

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'email',
			'password1'
			)

	def seve(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.email = self.cleaned_data['email']
		
		if commit:
			user.save()

		return user





