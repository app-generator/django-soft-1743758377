# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.TextField(max_length=255, null=True, blank=True)
    userpassword = models.TextField(max_length=255, null=True, blank=True)
    donvi = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    fullname = models.TextField(max_length=255, null=True, blank=True)
    picture = models.TextField(max_length=255, null=True, blank=True)
    phongban = models.TextField(max_length=255, null=True, blank=True)
    createdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modifydate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sgiindex(models.Model):

    #__Sgiindex_FIELDS__
    cs1 = models.IntegerField(null=True, blank=True)
    cs2 = models.IntegerField(null=True, blank=True)

    #__Sgiindex_FIELDS__END

    class Meta:
        verbose_name        = _("Sgiindex")
        verbose_name_plural = _("Sgiindex")



#__MODELS__END
