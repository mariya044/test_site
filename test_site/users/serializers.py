from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"

    def create(self,validated_data):
        return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.username=validated_data.get("username",instance.username),
        instance.first_name = validated_data.get("first_name", instance.first_name),
        instance.last_name = validated_data.get("last_name", instance.last_name),
        instance.password = validated_data.get("password", instance.password),
        instance.email = validated_data.get("email", instance.email),
        instance.save()
        return instance

