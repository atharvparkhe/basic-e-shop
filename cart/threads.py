import threading
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .utils import *

context = {}


class generate_invoice(threading.Thread):
    def __init__(self, order):
        self.order = order
        threading.Thread.__init__(self)
    def run(self):
        try:
            html_template = 'order.html'
            html_message = render_to_string(html_template, context)
            subject = 'Your Order Summary.'
            email_from = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject, html_message, email_from, [self.order.owner.email])
            msg.content_subtype = 'html'

            params = {
                "cart_obj" : self.order,
                "cart_items" : self.order.related_cart.all()
            }

            file_path, status = save_invoice(params)

            if status:
                path = "data/invoice/" + file_path + ".pdf"
                self.order.invoice = path
                self.order.save()
                msg.attach_file(path)
                msg.send()
            else : pass
        except Exception as e:
            print(e)

