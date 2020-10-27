# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

	imagen = models.FileField(upload_to="")
	bio    = models.CharField(max_length=120)
	fbook  = models.URLField(blank=True, null=True)
	igram  = models.URLField(blank=True, null=True)
	titer  = models.URLField(blank=True, null=True)
