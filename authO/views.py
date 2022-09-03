from django.shortcuts import render
from .service import Auth0Integration, AuthorizeAPI

# Create your views here.


class Auth0Service(Auth0Integration):
    Auth0Integration()

class AuthorizeService(AuthorizeAPI):
    AuthorizeAPI.as_view()


