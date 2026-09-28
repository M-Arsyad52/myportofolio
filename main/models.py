import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
        ("competition", "Competition"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(User, related_name="starred_experiences", blank=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        if self.ended_at is None:
            return True
        return self.ended_at > timezone.now()

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20,)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, default="")
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(User, related_name="starred_projects", blank=True)

    def __str__(self):
            return self.title

    @property
    def is_ongoing(self):
        if self.ended_at is None:
            return True
        return self.ended_at > timezone.now()

class Achievement(models.Model):
    LEVEL_CHOICES = [ ('campus', 'Campus'), ('national', 'National'), ('international', 'International')]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(
        choices=LEVEL_CHOICES,
        default='campus',
    )
    achieved_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def is_top_tier(self):
        if (self.level == 'national' or self.level == 'international'):
            return True