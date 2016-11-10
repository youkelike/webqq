from django.contrib import admin

from app import models,auth_admin
# Register your models here.
admin.site.register(models.QqGroup)
admin.site.register(models.UserGroup)
admin.site.register(models.UserProfile,auth_admin.UserProfileAdmin)
