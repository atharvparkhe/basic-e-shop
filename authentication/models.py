from django.db import models
from base.models import *


class CustomerModel(BaseUser):
    otp = models.CharField(max_length=6,null=True, blank=True)
    def __str__(self):
        return self.email