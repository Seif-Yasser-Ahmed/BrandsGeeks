from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'seifjamaica991@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587


def send_confirmation_email(user):
    subject = 'Welcome to my website'
    html_message = render_to_string('confirmation_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = 'your_email@example.com'
    to_email = user.email
    send_mail(subject, plain_message, from_email, [
              to_email], html_message=html_message)
