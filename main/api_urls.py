from django.urls import path
from main.api_views import (project_list, 
                            project_detail, 
                            project_star, 
                            experience_list,
                            experience_detail,
                            experience_star,
                            )

app_name = "api"
urlpatterns = [
    path("projects/", project_list, name="project-list"),
    path("projects/<uuid:project_id>/", project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", project_star, name="project-star"),

    path("experiences/", experience_list, name="experience-list"),
    path("experiences/<uuid:experience_id>/", experience_detail, name="experience-detail"),
    path("experiences/<uuid:experience_id>/star/", experience_star, name="experience-star"),
]