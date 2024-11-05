# calc/models.py
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    muscle_groups = models.CharField(max_length=200)
    equipment_needed = models.CharField(max_length=100)
    common_mistakes = models.TextField()
    variations = models.TextField(blank=True)
    sets_reps = models.TextField()  # Example: "3 sets of 10 reps"
    image = models.ImageField(upload_to='exercises/', blank=True)
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])

    def __str__(self):
        return self.name
