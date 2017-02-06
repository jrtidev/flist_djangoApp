from django.shortcuts import render, HttpResponse
from .forms import GuestForm

guests = {}
# Create your views here.
def main(request):
	return render(request, 'main/main.html')

#form for adding guest
def add_guest(request):
	if request.method == 'POST':
		form = GuestForm(request.POST)
		if form.is_valid():
			guestName = form.cleaned_data['guestName']
			guestEmail = form.cleaned_data['guestEame']
			guests[guestName][guestName]=guestEmail
		else: 
			form = GuestForm()
	return render(request, 'main/main.html', {'form': form})
