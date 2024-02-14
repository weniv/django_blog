from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all().order_by("-created_at")
    data = {"posts": posts}
    return render(request, "blog/post_lists.html", data)


def post_details(request, pk):
    post_data = Post.objects.get(pk=pk)
    data = {"post": post_data}

    return render(request, "blog/post_detail.html", data)

def new_post(request):
    return render(request, "blog/post_new.html")
