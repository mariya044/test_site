from django.core.mail import send_mail
from rest_framework import serializers
from users.models import User
from test_site import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"

    def create(self,validated_data):
        user=User.objects.create_user(
            validated_data["username"],
            validated_data["password"],
            validated_data["email"],
        )
        send_mail(
            'Thanks for registration',
            "Nice to meet you!",
            settings.DEFAULT_FROM_EMAIL,
            [validated_data['email']],
            fail_silently=False
        )
        return user

    def update(self,instance,validated_data):
        instance.username=validated_data.get("username",instance.username),
        instance.password = validated_data.get("password", instance.password),
        instance.email = validated_data.get("email", instance.email),
        instance.save()
        return instance



