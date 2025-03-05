from django.db import models
from django.utils.timezone import now

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Unknown Author")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
