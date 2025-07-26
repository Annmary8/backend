from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Design', 'Design'),
        ('Marketing', 'Marketing'),
        # Add more if needed
    ]

    RESOURCE_TYPE_CHOICES = [
        ('Course', 'Course'),
        ('Tutorial', 'Tutorial'),
        ('Book', 'Book'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('Started', 'Started'),
        ('Completed', 'Completed'),
    ]

    PLATFORM_CHOICES = [
        ('Udemy', 'Udemy'),
        ('Coursera', 'Coursera'),
        ('YouTube', 'YouTube'),
        ('Other', 'Other'),
    ]

    skill_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPE_CHOICES)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    hours_spent = models.PositiveIntegerField(default=0)
    difficulty_rating = models.IntegerField(default=1)  # Range: 1 to 5
    estimated_hours = models.PositiveIntegerField(null=True, blank=True)
    resource_url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill_name
