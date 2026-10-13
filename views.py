from django.shortcuts import render, redirect
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'posts/home.html', {
        'posts': posts
    })


def create_post(request):

    if request.method == 'POST':

        content = request.POST.get('content')
        image = request.FILES.get('image')

        if request.user.is_authenticated:
            Post.objects.create(
                user=request.user,
                content=content,
                image=image
            )

            return redirect('home')

    return render(request, 'posts/create_post.html')