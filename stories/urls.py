from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile_view, edit_profile, delete_profile

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('story_list/', views.story_list, name='story_list'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('add_story/', views.add_story, name='add_story'),
    path('edit_story/<int:story_id>/', views.edit_story, name='edit_story'),
    path('delete_story/<int:story_id>/', views.delete_story, name='delete_story'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    path('story/<int:story_id>/like/', views.toggle_like, name='toggle_like'),
]