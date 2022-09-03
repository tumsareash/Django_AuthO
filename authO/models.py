from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    full_name   = models.CharField(max_length=50)
    picture     = models.CharField(max_length=255)
    email       = models.EmailField(max_length=50) 

    def __str__(self):
        return self.full_name
    

class AuthorizeResponse(models.Model):
    access_token  = models.TextField()
    scope         = models.CharField(max_length=200)
    expiration    = models.IntegerField()
    token_type    = models.CharField(max_length=60)
    state         = models.TextField()
    user          = models.OneToOneField(UserProfile, on_delete=models.CASCADE)