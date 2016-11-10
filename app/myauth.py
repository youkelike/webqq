from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

#createsuperuser命令就是用的BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('email not provieded!')
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            #还有一些内置的字段
            #token = token,
            #department = department,
            #tel = tel,
            #memo = memo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name='邮箱',max_length=64,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    name = models.CharField(u'名字',max_length=32)
    token = models.CharField(u'token',max_length=128,default=None,blank=True,null=True)
    department = models.CharField(u'部门',max_length=32,default=None,blank=True,null=True)
    tel = models.CharField(u'座机',max_length=32,default=None,blank=True,null=True)
    mobile = models.CharField(u'手机',max_length=32,default=None,blank=True,null=True)
    memo = models.TextField(u'备注',default=None,blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True,blank=True)

    user_groups = models.ManyToManyField('UserGroup')
    friends = models.ManyToManyField('self', related_name='my_friends', blank=True)
    online = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u'用户信息'

    objects = UserManager()