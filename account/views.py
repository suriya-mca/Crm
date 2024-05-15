import secrets
import string
import datetime
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.template.loader import render_to_string
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
		user.save()

		messages.success(request, 'Registered Successfully 👍')
		return HttpResponseClientRedirect('/auth/login')
		   
	return render(request, 'pages/auth/register.html')


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

def send_reset_email(email, token):

    subject = 'Password Reset'
    reset_url = f'http://localhost:8000/auth/reset_password/{token}'
    html_message = render_to_string('email/reset_password_email.html', {'reset_url': reset_url})
    from_email = 'dummy@gmail.com'
    send_mail(subject, None, from_email, [email], html_message=html_message)

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
		send_reset_email(email, reset_token)
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