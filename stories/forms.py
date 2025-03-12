# In stories/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Story
from .models import Profile
from .models import Comment

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash password before saving
        if commit:
            user.save()
        return user

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
            model = Comment
            fields = ['content']