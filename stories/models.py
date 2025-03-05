from django.db import models
from django.utils.timezone import now

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
