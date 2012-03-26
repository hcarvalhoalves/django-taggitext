from django.db import models

from taggitext.managers import TaggableManager


class Page(models.Model):
    title = models.CharField(max_length=255)
    tags = TaggableManager()
