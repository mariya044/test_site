from django.contrib import admin
from users.models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display = ["email", "phone_number"]


admin.site.register(User, UserModelAdmin)
