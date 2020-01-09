from django.contrib import admin
from account.models import Profile
# Register your models here.

class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','email','password','user',)

admin.site.register(Profile, ProfilesAdmin)
