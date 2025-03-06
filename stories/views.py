from django.shortcuts import render, get_object_or_404, redirect
from .models import Story
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# This is a view function that returns a list of stories.
def story_list(request):
    stories = Story.objects.all().order_by('-created_at')
    return render(request, 'stories/story_list.html', {'stories': stories})
# this is a view function that returns a single story.  
def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    print(story.content)  # Debugging line
    return render(request, 'stories/story_detail.html', {'story': story})
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