from typing import Any
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User, related_name='members')
    messages = models.ManyToManyField('Message', related_name='messages', blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    belong = models.ManyToManyField(Group, related_name='belong')
    message = models.CharField(max_length=1000)
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message
    class Meta:
        ordering = ['time']
