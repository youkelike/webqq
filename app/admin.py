from django.contrib import admin
from app import models
# Register your models here.
admin.site.register(models.QqGroup)
admin.site.register(models.UserGroup)
admin.site.register(models.UserProfile)
