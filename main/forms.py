from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, Textarea
from main.models import Project, Experience


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title","type", "description", "tech_stack", "started_at", "ended_at"]

        labels = {
            "title": "Project Name",
            "description": "Project Description",
            "type": "Project Type (Personal/Group)",
            "tech_stack": "Technology Used",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g., Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "type": TextInput(
                attrs={
                    "placeholder": "e.g., Personal/Group",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "e.g., Django, Python, HTML, CSS",
                }
            ),
            "started_at": forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    "type": "datetime-local", "class": "form-control"
                }
            ),
            "ended_at": forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    "type": "datetime-local", "class": "form-control"
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category"]

        labels = {
            "title": "Experience Name",
            "description": "Experience Description",
            "category": "Experience Category",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g., Hackathon",
                        "maxlength": 255,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "e.g., Competition"
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your experience",
                        "rows": 3,
                }
            ),
        }