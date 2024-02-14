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
    if request.user.is_authenticated:

        post_data = Post.objects.get(pk=pk)
        if post_data.author_id == request.user.pk:
            data = {"post": post_data}

            return render(request, "blog/post_detail.html", data)
        else:
            return redirect("blog:post_list")

    else:
        return redirect("accounts:login")


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
        return render(request, "blog/post_new.html")
