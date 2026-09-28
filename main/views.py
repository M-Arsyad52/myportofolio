from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied        
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import datetime

from main.forms import ProjectForm, ExperienceForm, AchievementForm
from main.models import Experience, Project, Achievement

#=========
# PROFILE
#=========
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    
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
        "last_login": last_login
    }
    return render(request, "index.html", context)

#=============
# EXPERIENCES
#=============
def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    json_response = get_experience_json(request)
    
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [item.object for item in experiences]

    context = {
        "initial_name": "M Arsyad A",
        "name": "Arsyad",
        "page_title": "Experience List",
        "title_query": title_query,
        "experience_list": experiences,
        
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new experience has been added!")
        return redirect("main:show_experience")

    context = {
        "name": "Arsyad",
        "page_title": "Add Experience",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    data = serializers.serialize("json", experience)
    return HttpResponse(data, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success("Experience updated successfully")
        return redirect("main:show_experience")

    context = {
        "name": "Arsyad",
        "page_title": "Edit Experience",
        "form": form,
    }

    return render(request, "project.html", context)

#==========
# PROJECTS
#==========
def show_project(request):
    json_response = get_project_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [item.object for item in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "initial_name": "M Arsyad A",
        "name": "Arsyad",
        "page_title": "Project List",
        "title_query": title_query,
        "project_list": projects,
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "A new project has been added!")
        return redirect("main:show_project")

    context = {
        "name": "Arsyad",
        "page_title": "Add Project",
        "form": form,
    }
    return render(request, "project_form.html", context)

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated successfully.")
        return redirect("main:show_project")
    
    context = {
        "name": "Arsyad",
        "page_title": "Edit Project",
        "form": form,
    }
    return render(request, "project_form.html", context)

#==============
# ACHIEVEMENTS
#==============
def show_achievement(request):
    title_query = request.GET.get("title", "").strip()
    json_response = get_achievement_json(request)
    deserialized = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    achievements = [item.object for item in deserialized]
    #achievements = Achievement.objects.all().order_by("-achieved_at")
    
    context = {
        "name": "Arsyad",
        "page_title": "Achievement List",
        "achievement_list": achievements,
        "title_query": title_query,
    }
    return render(request, "achievement.html", context)

def create_achievement(request):
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_achievement")

    context = {
        "name": "Arsyad",
        "form": form,
        "page_title": "Add Achievement"
    }
    return render(request, "achievement_form.html", context)

def edit_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)
    form = AchievementForm(request.POST or None, instance=achievement)

    if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("main:show_achievement")

    context = {
            "name": "Arsyad",
            "form": form,
            "page_title": "Edit Achievement"
        }

    return render(request, "achievement_form.html", context)

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)
    if request.method == "POST":
        achievement.delete()

    return redirect("main:show_achievement")

def get_achievement_json(request):
    title_query = request.GET.get("title", "").strip()
    achievements = Achievement.objects.all().order_by("-achieved_at")

    if title_query:
        achievements = achievements.filter(title__icontains=title_query)

    data = serializers.serialize("json", achievements)

    return HttpResponse(data, content_type="application/json")

#==========
# Register, Login
#==========

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Arsyad",
        "page_title": "Register Account",
        "form": form
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
            "name": "Arsyad",
            "page_title": "Login Account",
            "form": form
        }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request,project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")