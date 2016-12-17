from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    websiteUrl = models.CharField(max_length=100,unique=True)
    callbackUrl = models.CharField(max_length=100, blank=True, null=True)
    temporaryCredentialsRequestUrl = models.CharField(blank=True, max_length=100)
    adminAuthorizationUrl  = models.CharField(blank=True, max_length=10)
    accessTokenRequestUrl = models.CharField(blank=True, max_length=10)
    consumerKey = models.CharField(blank=True, max_length=10)
    consumerSecret = models.CharField(blank=True, max_length=10)
    access_token = models.CharField(blank=True, max_length=10)
    refresh_token = models.CharField(blank=True, max_length=10)


    REQUIRED_FIELDS = ['callbackUrl',
                       'temporaryCredentialsRequestUrl',
                       'adminAuthorizationUrl',
                       'accessTokenRequestUrl',
                       'consumerKey',
                       'consumerSecret',
                       'access_token',
                       'refresh_token',
                       'websiteUrl']