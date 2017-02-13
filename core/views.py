from django.shortcuts import render, HttpResponse
from django.contrib import auth
from .forms import GuestForm, ItemForm, RegistrationForm
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View 


guests = {}
goods = {}

def home(request):
	return render(request, 'main/base.html')

def addGuest(request):
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
	return render(request, 'main/addGuest.html', context)

def addItem(request):
	addItemMessage = 'Please enter item that you need'
	itemForm = ItemForm(request.POST or None)
	if itemForm.is_valid():
		itemName = itemForm.cleaned_data['itemName']
		itemQtt = itemForm.cleaned_data['itemQtt']
		if itemName in goods.values():
			print('Dublicate item')
		else:
			goods[itemName]=itemQtt
			print(goods)
		itemForm = ItemForm()

	context={
		'form':itemForm,
		'addItemMessage':addItemMessage,
		'goods':goods,
	}
	return render(request, 'main/addItem.html', context)

def sendMessage(request):

	return render(request, 'main/sendMessage.html')

# user registrstion 
def addAccount(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main/addguest/')
	else:
		form = RegistrationForm()
		
		context = {'form':form}
		return render(request, 'main/registration.html', context)

























def send_message(guest, item):
    recipient = guests[guest]
    sender_lgn = 'tarartem@gmail.com'
    sender_pwd = 'Goo979198033'
    subj = 'Task from Artem'
    email_body = 'Hello, ' + guest + '! '+'\n' + 'Unfortunately we have forgoten to bye some staff for our festive table. Would you be so kinde to take with you following goods: ' + '\n' + goods[item] + ' of ' + item 

    msg = MIMEMultipart('alternative')
    smtpsrvr = smtplib.SMTP('smtp.gmail.com', 587)
    smtpsrvr.ehlo()
    smtpsrvr.starttls()
    smtpsrvr.ehlo()
    smtpsrvr.login(sender_lgn, sender_pwd)

    msg['Subject'] = subj
    msg['From'] = sender_lgn
    body = email_body

    content = MIMEText(body, 'plain')
    msg.attach(content)
    smtpsrvr.sendmail(sender_lgn, recipient, msg.as_string())
    smtpsrvr.close()










