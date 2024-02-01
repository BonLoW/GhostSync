from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    description = models.TextField(default='这个人木有写甚么',max_length=200)
    avatar_width = models.IntegerField(default=200)
    avatar_height = models.IntegerField(default=200)
    avatar = models.ImageField(upload_to='static/img/avatars',width_field='avatar_width',height_field='avatar_height' ,default='avatars/default.png')
    def __str__(self):
        return self.username

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    setter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='setter')
    description = models.TextField(default='这个群木有写甚么',max_length=200)
    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=200,blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    belong = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='belong')
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content