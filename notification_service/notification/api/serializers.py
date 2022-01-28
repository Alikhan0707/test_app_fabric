from rest_framework import serializers
from ..models import Notification, Client


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['text', 'start_at', 'end_at', 'mobile_operator_code', ]

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.start_at = validated_data.get('start_at', instance.start_at)
        instance.end_at = validated_data.get('end_at', instance.end_at)
        instance.mobile_operator_code = validated_data.get('mobile_operator_code', instance.mobile_operator_code)
        instance.save()

        return instance


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['phone_number', 'mobile_operator_code', ]

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.mobile_operator_code = validated_data.get('mobile_operator_code', instance.mobile_operator_code)
        instance.save()

        return instance
