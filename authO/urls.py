from django.urls import path
from authO import views


urlpatterns = [
    
    path('login_uri', views.Auth0Service.login_service, name='login'),
    path('home',views.Auth0Service.home,name='home'),
    path('Authorize',views.AuthorizeService.as_view(),name='Authorize'),

    
]
