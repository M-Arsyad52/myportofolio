from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Arsyad",
        "npm": "2506556246",
        "study_program": "Bachelor International Computer Science",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Arsyad",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)