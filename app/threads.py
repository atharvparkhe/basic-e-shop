from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import threading

context = {}
# context["site_url"] = settings.FRONTEND_URL


class send_contact_email(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            html_template = 'contact.html'
            html_message = render_to_string(html_template, context)
            subject = 'Thanks for filling up Contact Us form.'
            email_from = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject, html_message, email_from, [self.email, settings.ADMIN_EMAIL])
            msg.content_subtype = 'html'
            msg.send()
        except Exception as e:
            print(e)