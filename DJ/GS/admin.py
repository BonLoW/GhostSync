from django.contrib import admin
from .models import User, Group, Message

# Register your models here.
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Message)