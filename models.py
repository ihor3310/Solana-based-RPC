from django.db import models
from django.utils import timezone

class HistoryOfAllRequests(models.Model):
    last_request = models.CharField(null=True, max_length=100)
    count = models.IntegerField(null=True)
    note = models.TextField(null=True, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.last_request}, {(self.created_at)}, {(self.count)}'

class RegistrationRequest(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return f'{self.username}, {self.email}, {self.created_at}'
