from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import forms as auth_form

from app.myauth import UserProfile


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('email','token')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords donot match')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label='Password',
        help_text=('Raw password is not stored, so you cannot see it, but you can change it using <a href="/admin/password_change/">this form</a>'))

    def clean_password(self):
        return self.initial['password']

    class Meta:
        model = UserProfile
        fields = ('email','password','is_active','is_admin')

class UserProfileAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','is_admin','password')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Personal info',{'fields':('name','department','tel','mobile','memo')}),
        ('API TOKEN info',{'fields':('token',)}),
        ('Permissions',{'fields':('is_active','is_admin')}),
        ('Relationship',{'fields':('friends','user_groups')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_active','is_admin')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
