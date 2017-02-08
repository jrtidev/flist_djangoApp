from django import forms

class GuestForm(forms.Form):
	guestName = forms.CharField(max_length=100, required=False)
	guestEmail = forms.EmailField(max_length=100, required=False)