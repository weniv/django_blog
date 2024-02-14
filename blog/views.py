from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url="accounts:login")
def home(request):
    user_pk = request.user.pk
    posts = Post.objects.filter(author=user_pk).order_by("-created_at")
    data = {"posts": posts}
    return render(request, "blog/post_lists.html", data)


@login_required(login_url="accounts:login")
def post_details(request, pk):

    post_data = Post.objects.get(pk=pk)
    if post_data.author_id == request.user.pk:
        data = {"post": post_data}

        return render(request, "blog/post_detail.html", data)
    else:
        return redirect("blog:post_list")


@login_required(login_url="accounts:login")
def post_update(request, pk):
    post_data = Post.objects.get(pk=pk)
    if post_data.author_id == request.user.pk:
        if request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")
            post_data.title = title
            post_data.content = content
            post_data.save()
            return redirect("blog:post_list")
        else:
            data = {"post": post_data}
            return render(request, "blog/post_update.html", data)
    else:
        return redirect("blog:post_list")


@login_required(login_url="accounts:login")
def post_new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user_pk = request.user.pk
        post = Post(title=title, content=content, author_id=user_pk)
        post.save()
        return redirect("blog:post_list")
    else:
        return render(request, "blog/post_update.html")
