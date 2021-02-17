from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Alert(models.Model):
    message = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    asset_id = models.CharField(max_length=180, default='BTC')
    min_value = models.FloatField(default=5000)
    max_value = models.FloatField(default=7000)

    def __str__(self):
        return self.message
