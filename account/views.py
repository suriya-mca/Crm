import secrets
import string
import datetime
import threading
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django_htmx.http import retarget, HttpResponseClientRedirect, HttpResponseClientRefresh

from .models import UserToken


@require_http_methods(["GET", "POST"])
def register(request):

	if request.htmx:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		if not password == confirm_password:
			response = HttpResponse("Confirm pasword not matching")               
			return retarget(response, '#danger-confirm-password')

		if User.objects.filter(username=username).exists():
			response = HttpResponse("User name taken")               
			return retarget(response, '#danger-username')
			
		if User.objects.filter(email=email).exists():
			response = HttpResponse("Email already exists")               
			return retarget(response, '#danger-email')
            
		user = User.objects.create_user(username=username, email=email, password=password)
		user.is_active = False 
		user.save()

		verify_token = generate_token()
		expiration_date = timezone.now() + datetime.timedelta(minutes=10)
		user_token = UserToken.objects.create(user=user, token=verify_token, expiration_date=expiration_date)
		user_token.save()

		url = 'https://8000-monospace-cms-1715854674699.cluster-mwrgkbggpvbq6tvtviraw2knqg.cloudworkstations.dev/auth/verify_account'
		message = 'email/verify_account_email.html'
		subject = 'Account Verification'
		send_reset_email_thread(email, verify_token, url, message, subject)

		messages.success(request, 'Registered Successfully! Check your mail & verify')
		return HttpResponseClientRedirect('/auth/login')
		   
	return render(request, 'pages/auth/register.html')


@require_GET
def verify_account(request, token):

	if token:
		user_token = UserToken.objects.filter(token=token).first()

		if not user_token:
			response = "⚠️ Invalid or expired token"
			context = {'message': response}               
			return render(request, 'pages/auth/verify_account.html', context)
			
		if user_token.is_expired():
			response = "⚠️ Token has expired"
			context = {'message': response}
			return render(request, 'pages/auth/verify_account.html', context)

		user = user_token.user
		user.is_active = True
		user.save()
		user_token.mark_as_used()

		response = "Account verified successfully 👍"              
		message = {'message': response}
		return render(request, 'pages/auth/verify_account.html', message)

	return render(request, 'pages/auth/verify_account.html')


@require_http_methods(["GET", "POST"])
def login(request):

	if request.htmx:
		username = request.POST['username']
		password = request.POST['password']

		if not User.objects.filter(username=username).exists():
			response = HttpResponse("Username not exists")               
			return retarget(response, '#danger-username')

		user = auth.authenticate(username=username, password=password)

		if user is None:
			response = HttpResponse("Re-check the password")               
			return retarget(response, '#danger-password')

		auth.login(request, user)
		return HttpResponseClientRedirect('/auth/register')
       
	return render(request, 'pages/auth/login.html')


@require_GET
def logout(request):

    auth.logout(request)
    return redirect('login')


def generate_token(length=20):

    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def send_reset_email(email, token, url, message, subject):

    subject = subject
    reset_url = f'{url}/{token}'
    html_message = render_to_string(f'{message}', {'reset_url': reset_url})
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, None, from_email, [email], html_message=html_message)

def send_reset_email_thread(email, token, url, message, subject):

	thread = threading.Thread(target=send_reset_email, args=(email, token, url, message, subject))
	thread.start()

@require_http_methods(["GET", "POST"])
def forgot_password(request):

	if request.htmx:
		email = request.POST['email']
		user = User.objects.filter(email=email).first()

		if user is None:
			response = HttpResponse("Email not found")               
			return retarget(response, '#danger-email')

		reset_token = generate_token()
		expiration_date = timezone.now() + datetime.timedelta(minutes=10)
		user_token = UserToken.objects.create(user=user, token=reset_token, expiration_date=expiration_date)
		user_token.save()

		url = 'https://8000-monospace-cms-1715854674699.cluster-mwrgkbggpvbq6tvtviraw2knqg.cloudworkstations.dev/auth/reset_password'
		message = 'email/reset_password_email.html'
		subject = 'Password Reset'
		send_reset_email_thread(email, reset_token, url, message, subject)

		response = HttpResponse("Email Sent ✔️")               
		return retarget(response, '#email-button')

	return render(request, 'pages/auth/forget_password.html')


@require_http_methods(["GET", "POST"])
def reset_password(request, token):

	if request.htmx:
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		user_token = UserToken.objects.filter(token=token).first()

		if not user_token:
			messages.warning(request, '⚠️ Invalid or expired token')
			return HttpResponseClientRefresh()
        
		if user_token.is_expired():
			messages.warning(request, '⚠️ Token has expired')
			return HttpResponseClientRefresh()

		if not password == confirm_password:
			response = HttpResponse("Confirm pasword not matching")               
			return retarget(response, '#danger-confirm-password')

		user = user_token.user
		user.set_password(password)
		user.save()
		user_token.mark_as_used()
		
		messages.success(request, 'Password reset successfully 👍')
		return HttpResponseClientRefresh()

	context = {"token": token}
	return render(request, 'pages/auth/reset_password.html', context)