from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Arslan Syed',
        'title': 'Why I love Movies',
        'content': 'First Post Content',
        'date_posted': 'August 19, 2020',
    },
    {
        'author': 'Sidra',
        'title': 'Why I hate Movies',
        'content': 'Second Post Content',
        'date_posted': 'August 18, 2020',
    }
]


def home(request):

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': 'About'})
