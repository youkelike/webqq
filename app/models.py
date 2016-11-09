from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    user_groups = models.ManyToManyField('UserGroup')
    friends = models.ManyToManyField('self',related_name='my_friends',blank=True)
    online = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.name

class QqGroup(models.Model):
    name = models.CharField(max_length=64)
    founder = models.ForeignKey(UserProfile)
    brief = models.TextField(max_length=1024,default='nothing...')
    admin = models.ManyToManyField(UserProfile,related_name='group_admins')
    members = models.ManyToManyField(UserProfile,related_name='group_members')
    member_limit = models.IntegerField(default=20)
    def __str__(self):
        return self.name