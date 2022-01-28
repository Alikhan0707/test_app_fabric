from django.urls import path, include

urlpatterns = [
    path('api/', include(('notification.api.urls', 'api'), namespace='api'))
]