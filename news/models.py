from django.db import models
from datetime import datetime
from django.utils import timezone

class HackerNewsID(models.Model):
    hackernews = models.BigIntegerField(unique=True, primary_key=True)
    fetched_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.id = self.hackernews # replacing the id(primary key) as the hackernews id
        super(HackerNewsID, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.hackernews)