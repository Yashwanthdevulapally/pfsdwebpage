# Generated by Django 5.1.2 on 2024-10-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('muscle_groups', models.CharField(max_length=200)),
                ('equipment_needed', models.CharField(max_length=100)),
                ('common_mistakes', models.TextField()),
                ('variations', models.TextField(blank=True)),
                ('sets_reps', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='exercises/')),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
            ],
        ),
    ]
