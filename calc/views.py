from django.shortcuts import render
from .models import Exercise  # Import the Exercise model

def home(request):
    return render(request, 'calc/home.html')

def dashboard(request):
    return render(request, 'calc/dashboard.html')

def workout_plan(request):
    return render(request, 'calc/workout_plan.html')

def nutrition(request):
    return render(request, 'calc/nutrition.html')

def profile(request):
    if request.method == 'POST':
        # Process the data from the form
        name = request.POST.get('name')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        goal = request.POST.get('goal')

        # Here you might save this data to the database or perform some action.
        print(f"Name: {name}, Age: {age}, Height: {height}, Weight: {weight}, Goal: {goal}")

        # Redirect or render a success message/template
        return render(request, 'calc/profile.html', {'success': True})

    return render(request, 'calc/profile.html')

def exercise_library(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    exercises = Exercise.objects.all()  # Fetch all Exercise records

    if query:
        exercises = exercises.filter(name__icontains=query)  # Filter based on query

    context = {
        'exercises': exercises,  # Pass the exercises to the template
        'query': query,          # Pass the query for displaying in the template
    }
    return render(request, 'calc/exercise_library.html', context)

def about(request):
    return render(request, 'calc/about.html')
