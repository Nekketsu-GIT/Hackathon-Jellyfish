from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
max_length = 50


class CommonInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='type your phone number')

    class Meta:
        abstract = True


class MyUser(CommonInfo):
    age = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.user.username
