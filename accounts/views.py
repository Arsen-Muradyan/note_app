from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
# Login Page View
def login(request):
  return render(request, 'accounts/login.html')
# Register Page View
def register(request):
  return render(request, 'accounts/register.html')
# Logout View
def logout_action(request):
  logout(request)
  return redirect("/")
# Register Action View
def register_action(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  email    = request.POST.get('email')
  confirm  = request.POST.get('confirm')
  user_email  = User.objects.filter(email=email)
  user_username = User.objects.filter(username=username)
  # Check Email Exists
  if user_email:
    messages.error(request, "Email Already Exists")
    return redirect('/accounts/register')
  # Check Username Exists
  if user_username:
    messages.error(request, 'Username already exists')
    return redirect('/accounts/register')
  else:
    # Check Password Confirmation
    if confirm == password:
      User.objects.create_user(username, email, password)
      return redirect('/accounts/login')
    else: 
      messages.error(request, "Failed Password Confirmation")
      return redirect('/accounts/register')
# Login Action View
def login_action(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  if username and password:
    user = authenticate(username=username, password=password)
    # Check username and password is valid
    if user is not None:
      auth_login(request, user)
      return redirect('/notes/')
    else:
      messages.error(request, "Username Or Password Not Valid")
      return redirect('/accounts/login')
  else:
    messages.error(request, "All Fields Required")
    return redirect("/accounts/login")
