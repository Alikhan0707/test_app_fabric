from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from .serializers import NotificationSerializer


class CreateNotificationView(views.APIView):
    parser_classes = [JSONParser]

    @csrf_exempt
    def post(self, request):
        data = NotificationSerializer(data=request.data)

        if data.is_valid(raise_exception=True):
            return Response(data.data)

    @csrf_exempt
    def put(self, request):
        data
