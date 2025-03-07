from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]