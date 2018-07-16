from django.shortcuts import render

from rest_framework import views, response, status

from .serializers import MessageSerializer

class MessageView(views.APIView):
    """ Returns a message POST-ed to it, i.e. echo. """

    def post(self, request, *args, **kwargs):
        """ Post returns the same message sent. """
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
