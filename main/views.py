from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ExperienceForm
from main.models import Experience, Project

# Profile
def show_main(request):
    context = {
        "initial_name": "M Arsyad A",
        "middle_name": "Arsyad",
        "full_name": "Muhammad Arsyad Avmeilputra",
        "npm": "2506556246",
        "study_program": "Bachelor International Computer Science",
        "bio": (
            "A Computer Science student at the Universitas of Indonesia. Currently undergoing "
            "the third semester."
        ),
    }
    return render(request, "index.html", context)

# Experience
def show_experience(request):
    json_response = get_experiences_json(request)
    
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "initial_name": "M Arsyad A",
        "middle_name": "Arsyad",
        "title_query": title_query,
        "experience_list": Experience.objects.all(),
        
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new experience has been added!")
        return redirect("main:show_experience")

    context = {
        "initial_name": "M Arsyad A",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experience)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Project, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

# Project
def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "initial_name": "M Arsyad A",
        "middle_name": "Arsyad",
        "title_query": title_query,
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new project has been added!")
        return redirect("main:show_project")

    context = {
        "initial_name": "M Arsyad A",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")