from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# custom validator to limit the number of words in a story
def validate_story_length(value):
    max_words = 500  
    if len(value.split()) > max_words:
        raise ValidationError(f'Maximum {max_words} words allowed.')

# model for stories
class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[validate_story_length])

    def __str__(self):
        return self.title

# model for profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image',blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
# model for comments
class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.story}"

# model for likes
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'story']

    def __str__(self):
        return f"{self.user.username} likes {self.story.title}"