from django.contrib import admin
from users.models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display = ["email", "username","phone_number"]
    search_fields = ("username","email")


admin.site.register(User, UserModelAdmin)


