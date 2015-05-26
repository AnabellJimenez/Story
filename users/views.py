from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



def index(request):
	from django.conf import settings
	print "settings", settings.PWD 
	return render(request, 'users/sign_in.html')#redirect?

def register(request):
	#print User.objects.all()
	return render(request, 'users/register.html')

def sign_up(request):
	#save user info from the html form

	first_name = request.POST["first_name"]
	# print first_name
	last_name =request.POST["last_name"]
	# print last_name
	name = request.POST["user_name"]
	# print name
	email = request.POST["email"]
	# print email
	password = request.POST["password"]
	# print password


	#create user using the Django User built in model
	user = User.objects.create_user(first_name = first_name, last_name = last_name, username=name,email=email,password=password)
	#save new user created
	user.save() 
	print User.objects.all()
	#render to login page
	return render(request, 'users/sign_in.html')#redirect?

def verify(request):
	# print "verifying"
	
	#save the user input from the login form
	username = request.POST["username"]
	password = request.POST["password"]
	print "\nusername:", username, "\n"

	# #verify the user is valid using autenticate
	user = authenticate(username = username, password = password)
	# print "\n **********user: ", user.username

	# #if there is a user entered (not empty fields)
	if user is not None:
		if user.is_active:
			login(request, user)#use the login imported method to verify the user
			#allow user to access member only page
			print "USER LOGGED IN"
			
			return HttpResponseRedirect(reverse('users:home'))
		else: 
			return HttpResponse("ACCOUNT ERROR")
	else:
		return HttpResponse("INVALID LOGIN")
	# return HttpResponse('GO HOME')

#HOME METHOD ALLOWS MEMBERS ACCESS IF THEY ARE VALID USERS
@login_required(login_url = login)
def home(request):
	#print request.user #CODE FOR TESTING 

	if request.user.is_authenticated():
		return render(request, 'users/home.html')
	else:
		return HttpResponse("CANNOT ACCESS PAGE")

def log_out(request):

	# return HttpResponse("LOGOUT")
	logout(request)
	return render(request, 'users/sign_in.html')

