from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    PLAN_IDS = (
        (1, 'Free'),
        (0, 'Development'),
        (2, 'Enterprise'),
    )

    ENABLE_IDS = (
        (1, True),
        (0, False),
    )

    # Magento parameters
    oauth_initiate_url = models.CharField(max_length=200, blank=True)
    admin_authorize_url = models.CharField(max_length=200, blank=True)
    access_token_url = models.CharField(max_length=200, blank=True)
    api_url = models.CharField(max_length=200, blank=True)
    consumer_key = models.CharField(max_length=100, blank=True)
    consumer_secret = models.CharField(max_length=100, blank=True)

    # Google Analytics parameters
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True )

    # Koob prefered settings
    enable_discount = models.BooleanField(choices=ENABLE_IDS,default=1, blank=True)
    per_discount = models.FloatField(default=0)

    # User's primary information
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    contact_no = models.CharField(max_length=100, blank=True)
    website_url = models.CharField(max_length=100, blank=True, unique=True)
    plan_id = models.IntegerField(choices=PLAN_IDS, blank=True, default=1)

    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)

    REQUIRED_FIELDS = ['oauth_initiate_url',
                       'admin_authorize_url',
                       'access_token_url',
                       'api_url',
                       'consumer_key',
                       'consumer_secret',
                       'access_token',
                       'refresh_token',
                       'enable_discount',
                       'per_discount',
                       'name',
                       'email',
                       'contact_no',
                       'website_url',
                       'plan_id',
                       'created',
                       'modified']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(MyUser, self).save(*args, **kwargs)

    class Meta:
        db_table = 'MyUser'