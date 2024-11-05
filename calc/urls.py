from django.urls import path
from .views import home, dashboard, workout_plan, nutrition, profile, exercise_library, about  # Import the about view

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('workout_plan/', workout_plan, name='workout_plan'),
    path('nutrition/', nutrition, name='nutrition'),
    path('profile/', profile, name='profile'),
    path('exercise_library/', exercise_library, name='exercise_library'),
    path('about/', about, name='about'),  # Add this line for the About page
    
]

