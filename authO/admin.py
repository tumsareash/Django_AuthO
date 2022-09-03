from django.contrib import admin
from .models import AuthorizeResponse, UserProfile
# Register your models here.


@admin.register(AuthorizeResponse)
class AuthorizeResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'access_token', 'scope', 'expiration', 'token_type', 'state']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id']
