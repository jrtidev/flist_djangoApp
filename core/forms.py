from django import forms

class GuestForm(forms.Form):
	guestName = forms.CharField(max_length=100)
	guestEmail = forms.CharField(max_length=100)