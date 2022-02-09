from django.shortcuts import render
from . import models


def posts_all(request):
    post = models.Post.objects.all()
    return render(request, "post_list.html", {"post": post})
