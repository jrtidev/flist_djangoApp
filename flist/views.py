from django.shortcuts import redirect

def loginRedirect(request):
	return redirect('main/login') 