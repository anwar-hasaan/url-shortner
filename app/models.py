from django.db import models

class URL(models.Model):
    url = models.URLField(max_length=1000, editable=False)
    short_url = models.URLField(max_length=100, null=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.url
    