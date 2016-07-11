# -*- coding: utf-8 -*-

from django.db import models

from django_stats2.fields import Stat
from django_stats2.mixins import StatsMixin


class Note(StatsMixin, models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()

    reads = Stat()
    edits = Stat(historical=True)
