import secrets
import string
import threading
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


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