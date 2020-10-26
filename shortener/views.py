from django.shortcuts import render, reverse
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import PBKDF2PasswordHasher

from .models import *

# Create your views here.

def index(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  return render(request, 'dashboard.html')

def register(request):
  if request.method == "POST":
    print(request.POST)
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email_address = request.POST['email_address']
    password = request.POST['password']
    password_confirmation = request.POST['conf_password']
    
    if password == password_confirmation:
      hasher = PBKDF2PasswordHasher()
      password = hasher.encode(password, salt = hasher.salt())
      user = User.objects.create(username = username, last_name = lastname, first_name = firstname, email = email_address, password = password)
      login(request, user = user)
      return HttpResponseRedirect(reverse('dashboard'))
    else:
      return render(request, 'register.html', context = {'firstname': firstname, 'username': username, 'lastname': lastname, 'email_address': email_address, 'password': '', 'conf_password': "", 'error': 'passwords do not match'})
  return render(request, 'register.html', context = {'firstname': '', 'username': '', 'lastname': '', 'password': '', 'conf_password': '', 'email_address': ''})

def login_user(request):
  if request.method == 'POST':
    user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
    if user is not None:
      login(request, user = user)
      return HttpResponseRedirect(reverse('dashboard'))
    else:
      return render(request, 'login.html', context = {'username': request.POST['username'], 'password': '', 'error': 'Invalid Credentials'})
  return render(request, 'login.html', context = {'username': '', 'password': ''})

def new_url(request):
  if request.method == "POST":
    pass
  return render(request, 'newurl.html')

def get_url(request, url_id):
  pass

