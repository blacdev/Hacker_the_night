from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
import json
import requests
import pusher

# Create your views here.
@api_view(['POST'])
def serve(request):
    data = json.loads((request.body))
    message = data["message"]
    pusher_client = pusher.Pusher(
    app_id='1286235',
    key='7799888a6bb007b7e9cd',
    secret='0444db8d50a705398faf',
    cluster='eu',
    ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event', {'message': message})

    return Response("succes")