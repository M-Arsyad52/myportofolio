from django.shortcuts import render

from main.models import Experience, Project


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


def show_experience(request):
    context = {
        "initial_name": "M Arsyad A",
        "middle_name": "Arsyad",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    context = {
        "initial_name": "M Arsyad A",
        "middle_name": "Arsyad",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)