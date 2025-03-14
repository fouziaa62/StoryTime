from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, Comment, Like
from .forms import CommentForm
from .forms import UserSignupForm, StoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from .forms import ProfileForm
from .models import Profile
from django import forms


@login_required
# This is a view function that returns a list of stories.
def story_list(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories})
  
# this is a view function that returns a signup form.
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserSignupForm()  # Show the empty form

    return render(request, 'registration/signup.html', {'form': form})

# This is a view function that requires the user to be logged in to access it.
@login_required
def home(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, "stories/story_list.html", {"stories": stories})

# This is a view function that returns a single story.

def story_detail(request, story_id):
    # Get the story or return 404 if not found
    story = get_object_or_404(Story, id=story_id)
    comments = story.comments.all()

    # Get the like count and check if the user has liked the story
    likes_count = Like.objects.filter(story=story).count()
    user_has_liked = Like.objects.filter(story=story, user=request.user).exists()

    # Handle POST request for submitting a new comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.save()
            return redirect('story_detail', story_id=story.id)  # Redirect to the same story page after saving comment
    else:
        form = CommentForm()  # Instantiate an empty form for GET request

    # Render the template with the story, comments, form, likes count, and user like status
    return render(request, 'stories/story_detail.html', {
        'story': story,
        'comments': comments,
        'form': form,
        'likes_count': likes_count,
        'user_has_liked': user_has_liked
    })

@login_required
def add_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('story_list')
    else:
        form = StoryForm()
    return render(request, 'stories/add_story.html', {'form': form})

@login_required
def edit_story(request, story_id):
    story = get_object_or_404(Story, id=story_id, author=request.user)
    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('story_detail', story_id=story.id)
    else:
        form = StoryForm(instance=story)
    return render(request, 'stories/edit_story.html', {'form': form})

@login_required
def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id, author=request.user)
    if request.method == 'POST':
        story.delete()
        return redirect('story_list')
    return render(request, 'stories/delete_story.html', {'story': story})
@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'stories/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'stories/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        user = profile.user
        profile.delete()
        user.delete()  # Also delete the user account if the profile is gone
        return redirect('login')
    return render(request, 'stories/delete_profile.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Ensure user has a profile
            Profile.objects.get_or_create(user=user)
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

class LikeForm(forms.Form):
    pass  

@login_required
def toggle_like(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, story=story)

    if not created:
        # If the like already exists, we delete it (unlike)
        like.delete()

    return redirect('story_detail', story_id=story.id)