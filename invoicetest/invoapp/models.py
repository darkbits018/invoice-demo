from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User

class Client(models.Model):
    #Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=100)

    #Utility Fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=True, unique=True, blank=True, null=True)