from django.contrib.auth.models import User
from rest_framework import serializers


# model serializer [similar to forms.ModelForm]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "position", "city")


# normal serializer [similar to forms.Form]
class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)

    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        return instance
