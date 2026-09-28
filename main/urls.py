from django.urls import path

from main.views import (show_main, 
                        show_experience, 
                        create_experience,
                        get_experience_json,
                        delete_experience,
                        edit_experience,
                        toggle_star_experience,

                        show_project, 
                        create_project, 
                        get_project_json, 
                        delete_project, 
                        edit_project,
                        toggle_star_project,

                        show_achievement,
                        create_achievement,
                        get_achievement_json,
                        delete_achievement,
                        edit_achievement,

                        register,
                        login_user,
                        logout_user,
                        )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experiences_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("edit-experience/<uuid:experience_id>/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),

    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("edit-project/<uuid:project_id>/", edit_project, name="edit_project"),
    path("project/<uuid:project_id>/star/", toggle_star_project, name="toggle_star_project"),

    path("achievement/", show_achievement, name="show_achievement"),
    path("achievement/add", create_achievement, name="create_achievement"),
    path("api/achievement/", get_achievement_json, name="get_achievement_json"),
    path("project/<uuid:achievement_id>/", delete_achievement, name="delete_achievement"),
    path("edit-achievement/<uuid:achievement_id>/", edit_achievement, name="edit_achievement"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]