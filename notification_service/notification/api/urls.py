from django.urls import path, include
from .views import NotificationViewSet, ClientViewSet, StatisticViewSet

notification_list = NotificationViewSet.as_view({'get': 'list', 'post': 'create'})
notification_detail = NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

client_list = ClientViewSet.as_view({'get': 'list', 'post': 'create'})
client_detail = ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

total_messages = StatisticViewSet.as_view({'get': 'general'})
notification_total_messages = StatisticViewSet.as_view({'get': 'notification_stat'})

urlpatterns = [
    path('notifications/', notification_list, name='notification_list'),
    path('notifications/<int:pk>/', notification_detail, name='notification_detail'),
    path('client/', client_list, name='client_list'),
    path('client/<int:pk>/', client_detail, name='client_detail'),
    path('general_stat/', total_messages, name='total_messages'),
    path('general_stat/<int:pk>/', notification_total_messages, name='notification_total_messages'),

]
