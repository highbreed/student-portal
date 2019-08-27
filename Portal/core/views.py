from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def home(request):
	return render(request, 'index.html')

@login_required(login_url='/login/')
def information_update(request):
	return render(request, 'information_update.html')

@login_required(login_url='/login/')
def fees(request):
	return render(request, 'fees.html')

@login_required(login_url='/login/')
def timetable(request):
	return render(request, 'timetable.html')

@login_required(login_url='/login/')
def course(request):
	return render(request, 'course.html')

@login_required(login_url='/login/')
def results(request):
    return render(request, 'results.html')

@login_required(login_url='/login/')
def requests(request):
    return render(request, 'request.html')


def Login(request):
	if request.method == 'POST':
		username = request.POST['regNo']
		password = request.POST['smisPass']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return redirect('/login/')
	else:
		return render(request, 'login.html')


def Logout(request):
	logout(request)
	return redirect('/login/')
