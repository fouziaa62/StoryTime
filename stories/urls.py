from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path("logout/", LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]