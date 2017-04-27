from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    context = {'test': 'JERSH'}
    return render(request, 'smuckers/index.html', context)

def display(request):
    context = {'test': 'JERSH'}
    return render(request, 'smuckers/display.html', context)

def enter(request):
    context = {'test': 'JERSH'}
    return render(request, 'smuckers/enter.html', context)

def loginUser(request):
    context = {'test': 'JERSH'}
    return render(request, 'smuckers/login.html', context)

def loginPost(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/smuckers')
	else:
		return redirect('/smuckers/login')

def logoutUser(request):
	logout(request)
	return redirect('/smuckers')