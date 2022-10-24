from django.db import models

class URL(models.Model):
    url = models.URLField(max_length=1000)
    short_url = models.URLField(max_length=100, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.url
    