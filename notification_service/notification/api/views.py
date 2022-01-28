from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Count

from .serializers import NotificationSerializer, ClientSerializer, NotificationStatSerializer
from ..models import Notification, Client, Message


class NotificationViewSet(ViewSet):

    def list(self, request):
        queryset = Notification.objects.all()
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Notification.objects.all()
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

    def create(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Notification.objects.all()
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Notification.objects.all()
        notification = get_object_or_404(queryset, pk=pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientViewSet(ViewSet):
    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Client.objects.all()
        notification = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(notification)
        return Response(serializer.data)

    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Client.objects.all()
        notification = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(notification, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Client.objects.all()
        notification = get_object_or_404(queryset, pk=pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatisticViewSet(ViewSet):
    def general(self, request):
        queryset = Message.objects.annotate(total_messages=Count('notification_id')).group_by('status')
        serializer = NotificationStatSerializer(queryset, many=True)
        return Response(serializer.data)

    def notification_stat(self, request, pk=None):
        queryset = Message.objects.filter(notification_id=pk).annotate(total_messages=Count('notification_id')).group_by('status')
        serializer = NotificationStatSerializer(queryset)
        return Response(serializer.data)
