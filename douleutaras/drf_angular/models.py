from django.db import models
import datetime

class User(models.Model):
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=75)

    def __unicode__(self):
        return self.username

class Todo(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    done = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today())
    user = models.ForeignKey(User, related_name='todos')

    def __unicode__(self):
        return self.title

