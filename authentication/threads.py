import threading, random
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .models import *

context = {}

class send_forgot_link(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            otp = random.randint(100001, 999999)
            cache.set(otp, self.email, timeout=350)
            context["otp"] = otp
            print(otp)
            html_template = 'forgot.html'
            html_message = render_to_string(html_template, context)
            subject = 'OTP to Verify your Account.'
            email_from = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject, html_message, email_from, [self.email])
            msg.content_subtype = 'html'
            msg.send()
        except Exception as e:
                print(e)


# class send_login_otp(threading.Thread):
#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)
#     def run(self):
#         try:
#             otp = random.randint(100001, 999999)
#             cache.set(otp, self.email, 350)
#             print(otp)
#             subject = "OTP to login into your account"
#             message = f"The OTP to log in into your email is {otp} \nIts valid only for 2 mins."
#             email_from = settings.EMAIL_HOST_USER
#             send_mail(subject , message ,email_from ,[self.email])
#         except Exception as e:
#             print(e)
