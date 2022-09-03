from django.shortcuts import render
from decouple import config
import requests
from django.http import JsonResponse

from .serializers import AuthorizeSerializer
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

# Create your views here.


class Auth0Integration:

    def login_service(request):
        response_type = 'token&'
        client_id = config('APP_CLIENT_ID')
        redirect_uri = 'http://127.0.0.1:8000/home'
        url = f'https://dev-jqa3s7io.us.auth0.com/authorize?response_type={response_type}client_id={client_id}&redirect_uri={redirect_uri}'
        headers={'Access-Control-Allow-Origin': "*", 'Accept': '*/*'}
        response = requests.get(url,headers=headers)
        print("response = ",response)
        r_url = response.url
        if response.status_code == 200:
            return JsonResponse({'redirect_url': r_url})
        else:
            return JsonResponse({'Response': response.status_code})

    def home(request, **kwargs):

        return render(request, 'home.html')


class AuthorizeAPI(APIView):
    @swagger_auto_schema(request_body=AuthorizeSerializer)
    def post(self, request, format=None):
        serializer = AuthorizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
