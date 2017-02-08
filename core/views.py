from django.shortcuts import render, HttpResponse
from .forms import GuestForm
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

guests = {}
def main(request):
	title = 'Application title'
	addGuestMessage = 'Please enter name and email of your guest'
	form = GuestForm(request.POST or None)
	if form.is_valid():
		guest = form.cleaned_data['guestName']
		email = form.cleaned_data['guestEmail']
		if email in guests.values():
			print('Dublicate guest')
		else:
			guests[guest]=email
			print(guests)
		form = GuestForm()
	context={
		'form':form,
		'addGuestMessage':addGuestMessage,
		'guests':guests,
	}
	return render(request, 'main/main.html', context)