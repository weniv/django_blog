from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path("", views.home, name="post_list"),
    path("post/<int:pk>/", views.post_details, name="post_details"),
    path("post/new/", views.post_new, name="post_new"),
]
