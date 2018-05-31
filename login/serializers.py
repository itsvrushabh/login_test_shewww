from rest_framework import serializers
from login.models import LoginDetail


class LoginDetailSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)
    host = serializers.IPAddressField(protocol='both')
    device_type = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return LoginDetail(id=None, **validated_data)
