from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_posted = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[f'{self.id}'])
