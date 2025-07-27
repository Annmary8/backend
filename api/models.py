from django.db import models
from django.contrib.auth.models import User

from django.db import models

from django.db import models

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    hours_spent = models.IntegerField()
    difficulty_rating = models.IntegerField()
    estimated_hours = models.IntegerField(default=0)
    resource_url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill_name


