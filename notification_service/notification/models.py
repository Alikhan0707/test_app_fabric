import uuid
from django.db import models
from django.core.validators import RegexValidator


class MobileOperatorCode(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Mobile operator code'
        verbose_name_plural = 'Mobile operator codes'


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField(null=False)
    start_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)
    mobile_operator_code = models.ForeignKey(MobileOperatorCode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('text', 'start_at')
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_regex = RegexValidator(regex=r'^7\d{9,10}$',
                                 message='Номер телефона должен начинаться с +7 и состоять из '
                                         '10 цифр включая код мобильного оператора')
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    mobile_operator_code = models.ForeignKey(MobileOperatorCode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('mobile_operator_code',)
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sent_at = models.DateTimeField()
    status = models.BooleanField(default=True)
    notification_id = models.ForeignKey(Notification, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('notification_id',)
        verbose_name = 'message'
        verbose_name_plural = 'messages'

