from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Story, Like, Comment
from .forms import CommentForm
from .forms import UserSignupForm, StoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from .forms import ProfileForm
from .models import Profile
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


# This is a view function that returns the landing page.
def landing_page(request):
    stories = Story.objects.all()[:6]  # Get the latest 6 stories
    print("Stories for Landing Page:", stories) 
    return render(request, 'landing.html', {'stories': stories})


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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, Comment, Like
from .forms import CommentForm

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
            comment.story = story  # Link the comment to the story
            comment.author = request.user  # Associate the comment with the current user
            comment.save()  # Save the comment to the database
            return redirect(reverse('story_detail', args=[story.id]) + '#comments-section')
              # Redirect to the same page to prevent resubmission
        else:
            print("Form is not valid:", form.errors)  # Log form errors for debugging

    else:
        form = CommentForm()  # Instantiate an empty form for GET requests

    # Render the template with context
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
            messages.success(request, "Story created successfully!")
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
            messages.success(request, "Story updated successfully!")
            return redirect('story_detail', story_id=story.id)
    else:
        form = StoryForm(instance=story)
    return render(request, 'stories/edit_story.html', {'form': form})

@login_required
def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id, author=request.user)
    if request.method == 'POST':
        story.delete()
        messages.error(request, "Story deleted successfully!")
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
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'stories/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.error(request, "Profile deleted successfully!")
        return redirect('landing_page')  # Replace 'landing_page' with the actual name of your landing page URL pattern
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



# notification messages 

@receiver(user_logged_in)
def login_success(sender, request, user, **kwargs):
    messages.success(request, f"Welcome back, {user.username}!")

@receiver(user_logged_out)
def logout_success(sender, request, user, **kwargs):
    messages.info(request, "You have been logged out successfully.")